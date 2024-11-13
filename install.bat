@echo off

echo Select...

echo Please run python loader

echo if your pc is 64 bit write 1 and if your pc is 32 bit write 2 : 

CHOICE /C 12C /M "bitness of your system : "
if %errorlevel% == 1
start https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe
start ..\python-3.13.0-amd64.exe
if %errorlevel% == 2
start https://www.python.org/ftp/python/3.13.0/python-3.13.0.exe
start ..\python-3.13.0.exe

echo if you have Windows 11, write a, and if you have Windows 7,8,10, write b : 
CHOICE /C ab /M "what windows do you have? : "
    if %errorlevel% == a
    start ..\main11.py 
    if %errorlevel% == b      
    start ..\main7,8,10.py