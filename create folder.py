import os
from datetime import date
import time

today = date.today()
print("Todays Date",today)


def Folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


print("Created Folder")
Folder('./'+str(today)+'/')
# Creates a folder in the current directory with todays date

    
