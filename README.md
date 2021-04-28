# Debian Create Launcher

**code file:** appfile.py  
**date:** Apr 2021  
**comments:**  
Python 3.7+  

Provides a GUI solution to create an application  
launcher for both **menu** and **desktop**.  

_Usually the "application.desktop" file is  
created by the application's install program.  
Some "Create Launcher's" only create the  
DESKTOP launcher._    

**Must be run as root**

Using:  

on debian distros:  

```
pkexec python3 FULLPATH/appfile.py
```

on Raspberry Pi:  

```
sudo python3 FULLPATH/appfile.py
```

Fields left blank are skipped with "Save".  
"Name", "Type", and "Exec" are required.

See the included PDF for a full list of  
other possible key=vaule pairs.


