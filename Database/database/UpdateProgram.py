#This Program utilizes the system terminal to download, sync, and install updates.
#If your terminal is blocked for security reasons. You may need to install updates manually.
#Please make sure git is installed. This script won't work without it.

#Import required moduels
import os #For file editing
import shutil #For folder deleting
import subprocess as sp
from custom_database import exit, clear #Used to close the app.

#Clear the system afer imports are finished.
clear()
#Remove Old UpdateFolder if it exists.
try:
    shutil.rmtree(
        "UpdateFolder"
)
except:
    #Folder doesn't exist
    pass
#Grab the latest source code and store it in a file called UpdateFolder
os.system('git clone https://github.com/sukadateam/database UpdateFolder')

#Check to see if the folder exists and all the needed items are present
#If any requirements are missing then terminate proccess and return an Error.
#Do Not Attempt to install to prevent data corruption!
output = sp.getoutput('cd UpdateFolder\ncd database\nls')
print ('\n\nFiles Downloaded\n',output)

#Search for command file. Used to determine what needs to be updated.
from UpdateCommands import UpdateRequirments, UpdateDatabase, UpdateSaveFile, UpdateApplication
print(
    "\n!Files downloaded!"
    "\nUpdate Settings:\n  UpdateRequirments: ",
    UpdateRequirments,'\n  UpdateDatabase:    ',
    UpdateDatabase,'\n  UpdateSaveFile:    ',
    UpdateSaveFile,'\n  UpdateApplication: ',
    UpdateApplication)

print("\nPre-install checks in progress...")
#Check to ensure all file required are present.
allChecksPass=True
if UpdateRequirments==True:
    if os.path.exists('requirements.txt') == True:
        print('  UpdateRequirments Test: Passed')
    else:
        print('  UpdateRequirments Test: Failed')
        allChecksPass=False
if UpdateDatabase==True:
    if os.path.exists('custom_database.py') == True:
        print('  UpdateDatabase Test: Passed')
    if os.path.exists('custom_database.py') == False:
        print('  UpdateDatabase Test: Failed')
        allChecksPass=False
if UpdateApplication==True:
    if os.path.exists('app.py') == True:
        print('  UpdateApplication Test: Passed')
    if os.path.exists('app.py') == False:
        print('  UpdateApplication Test: Failed')
        allChecksPass=False
#Save file does not need to be checked. As it wasn't downloaded.
if allChecksPass==False:
    print("One or more tests have failed. Continue? ")
    UserInput=input('Yes or No: ').lower()
    if UserInput=="no" or UserInput=="n":
        print("!Program will not terminate!")
        os._exit(1)