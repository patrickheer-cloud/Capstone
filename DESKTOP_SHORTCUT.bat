@echo off
echo Creating desktop shortcut...

set SCRIPT="%TEMP%\CreateShortcut.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = oWS.SpecialFolders("Desktop") ^& "\Django CRM.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "%~dp0START_CRM.bat" >> %SCRIPT%
echo oLink.WorkingDirectory = "%~dp0" >> %SCRIPT%
echo oLink.Description = "Django CRM System" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%

cscript /nologo %SCRIPT%
del %SCRIPT%

echo.
echo [√] Desktop shortcut created!
echo You can now start the CRM from your desktop.
echo.
pause