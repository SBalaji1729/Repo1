echo off 

rem : Windows batch script to invoke python script sel-gmail-chrome-win.py
rem : A desktop shortcut with ctrl-Key mapping can be created for quick-laumching the batch script 

cd  %USERPROFILE%\OneDrive\bin
py -3 sel-gmail-chrome-win.py

pause

exit 