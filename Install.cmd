::for windows users, run this first time, then run Run.cmd
::install python3.8
python-3.8.2.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
::run script to install pip utility
python3 get-pip.py
::this pkg is required to color the console
python3 -m pip install colorama
