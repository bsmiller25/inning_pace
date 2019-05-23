# inning_pace

My fantasy baseball league has an innings limit and ESPN stopped showing me my pace. So instead of calculating it everyday I created this!

## Note:
I wrote this quickly using Python 3.6 on Ubuntu 18. Setting up a desktop icon is probably different on Macs but I don't know. Also all file paths are written Unix style. Make necessary adjustments.

You will need Python3 with tkinter. You may need to run `apt-get install python3-tk` before setup. 

## Setup (for Ubuntu 18):

1) Clone this repo locally.

2) Set up the environment:   
`python3 -m venv venv`  

3) Install requirements:    
`pip install -r requirements.txt`

4) Edit pace.py for league specifications.   
-- Change the shebang to your venv location.  
-- My league is NL only, for something different, change `nl = standings()[3:]`.   
-- Change the pace formula as needed.  

5) Edit pace.desktop as needed.    
-- Update the Exec and Icon entries as appropriate.   

6) Make sure pace.py is executable.  
-- `chmod +x pace.py`    

6) Run  
-- If you haven't set up the desktop icon: `./pace.py`.  
-- If you have set up the desktop icon: double click and "Trust and Launch".  

7) Copy/Move desktop icon to desktop!
