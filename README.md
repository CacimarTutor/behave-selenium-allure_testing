# behave-selenium-allure_testing
A repository for API testing and UI testing using behave, selenium and allure in python

# Getting the Source
To start building the project, you need to grab the code from the repository. Follow these steps:
* Install git bash if on a windows machine
* Get the link to the code by clicking on code as below and click on the clipboard to copy the link as shown in this 
![Image](start.PNG?raw=true "Clone link")
* Run git bash from programs and once the window is open run the below command:
	* git clone (insert the link copied to the clipboard here)
* You should now have a copy of the source code

# Environment Setup
Before initiating the project make sure you have python installed. Then proceed with the following steps

#### Windows Machine
* Open the command prompt and run the following commands one after the other
	* pip install django
	* pip install django-tastypie
	* pip install selenium
	* pip install behave
	* pip install allure-pytest
	* pip install pytest-django
	* pip install allure-behave


* Open powershell and run as administrator. Then run the following commands
	* Set-ExecutionPolicy RemoteSigned -scope CurrentUser 
	* Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh') 
	* scoop install allure

#### Additional Requirements
* Download chrome driver to be used with selenium at https://chromedriver.chromium.org/downloads
* Create a folder in C:\ drive known as bin and copy the downloaded driver
* Add this folder(C:\bin) to the path environment using the procedure at https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/
* Install jenkins from https://www.jenkins.io/
* Install Google Chrome from https://www.google.com/chrome/
* Install Pycharm from https://www.jetbrains.com/pycharm/
* Install PostMan from https://www.postman.com/


### Starting the django project
* If you have a zip of the project extract it to get the folder: behave_selenium_allure_testing
* If you clone this repository you will already have this folder
* Open command prompt and run the following commands
	* cd behave_selenium_allure_testing
	* python manage.py runserver
	* [These commands will start the django application on localhost:8000]
	* Launch Google chrome and navigate to localhost:8000/admin
	* You should have the following page
	![Image](django.PNG?raw=true "Clone link")
	* [This is the interface to be used for performing tests using selenium]
##### Running the selenium test
* Open another command prompt and run the following command
	* cd sampleapi
	* python -m pytest 
	* [This will run the selenium test for testing the admin login and show the below output]
	![Image](seleniumtest.PNG?raw=true "Clone link")






