# behave-selenium-allure_testing
A repository for API testing and UI testing using behave and selenium

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
	* pip install allure-pytest
	* pip install pytest-django

* Open powershell and run as administrator. Then run the following commands
	* Set-ExecutionPolicy RemoteSigned -scope CurrentUser 
	* Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh') 
	* scoop install allure


