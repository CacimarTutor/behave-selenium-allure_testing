from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import allure
import pytest

# Create your tests here.
@allure.severity(allure.severity_level.NORMAL)
class LoginTest(LiveServerTestCase):
  @allure.severity(allure.severity_level.MINOR)
  def testform(self):
  	self.selenium = webdriver.Chrome()
  	#Choose your url to visit
  	self.selenium.get('http://127.0.0.1:8000/admin')
  	#find the elements you need to submit form
  	self.user_name = self.selenium.find_element_by_id('id_username')
  	self.password = self.selenium.find_element_by_id('id_password')
  	self.submit = self.selenium.find_element_by_xpath("//input[@value='Log in']")
  	#populate the form with data
  	self.user_name.send_keys('admin')
  	self.password.send_keys('admin')
  	#submit form
  	self.submit.send_keys(Keys.RETURN)
  	#check result; page source looks at entire html document
  	assert 'admin' in self.selenium.page_source
