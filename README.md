# PyTest_Selenium_Framework_Template
- Template repository for PyTest &amp; Selenium framework for test automation. 
- Elliot Erstein, 8 Dec 2021
**********************************************************************************************
## About
- This framework has examples to run both a website automation test and a windows application test.
- This template is meant to be the starting point to create new projects (via github) for different websites and applications.
**********************************************************************************************
## Automation framework required software dependencies
- Windows 10 64-Bit
- ChromeWebdriver
    - https://chromedriver.chromium.org/downloads
    - Chromedriver needs to match chrome.exe version (ex: Version 96.0.4664.93 (Official Build) (64-bit))
    - C:\DRIVERS\chromedriver.exe
    - Add to PATH
- WinAppDriver
  - https://github.com/Microsoft/WinAppDriver/releases
  - C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe
  - Add to PATH
- Python 3.10
  - https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe
  - Custom >> Add to PATH >> All users >> Install
- PyCharm IDE
  - https://www.jetbrains.com/pycharm/download/#section=windows
  - Install >> Add Bin to PATH
- Win10 SDK package (10.0.22000.194)
  - https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/
  - This is for the inspect.exe to find UI elements in windows applications
  - C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x64\inspect.exe
  - Create shortcut on desktop for future use
- Switch to Win10 Developer Mode  
  - In Windows type "Developer settings" >> Enable Developer Mode
- Git
  - https://git-scm.com/downloads
  - Install
**********************************************************************************************
## Required python packages
If this template is used, the required python packages are already installed in the virtual environment so this step is not needed. If starting from scratch, install the following packages in python.
install appium >> 
- pip install appium-python-client==1.3.0
  - The latest appium versions (2.1 & 2.0) use selenium 4.0 which would not run WinAppDriver correctly.
- pip install pytest pytest-html pytest-xdist Openpyxl
**********************************************************************************************
## Git commands for initial setup (JWOW repository only)
git init
git config --global user.email "{ID}+J-WoW18@users.noreply.github.com"
git add -A
git commit -m "First commit"
git remote add origin https://github.com/J-WoW18/PyTest_Selenium_Framework_Template.git 
git push origin master
**********************************************************************************************
## Resources: Guides, Videos, Documentation
- https://testautomationu.applitools.com/winappdriver-tutorial/ -- Tutorial video series for the calculator example
- https://www.youtube.com/watch?v=57pjD89IFXA -- Tutorial video series that was the basis for this framework template
- https://www.fleekitsolutions.com/use-winapp-driver-python/ -- Another example of how to setup WinAppDriver and Python
- https://selenium-python.readthedocs.io/index.html -- Documentation for Selenium-Python
