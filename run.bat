REM These are example commands to run the template tests for either a website or the calculator example
REM For the calculator example -- need to have the WinAppDriver.exe already running
REM ### Website example commands
REM pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome --capture=tee-sys
REM pytest -s -v --html=./Reports/report.html testCases/test_login.py --browser chrome --capture=tee-sys
REM ### Calculator example commands
pytest -s -v -m calc --html=./Reports/report.html testCases/ --browser windows --capture=tee-sys
