#Terminal Version to download and install updates. A Visual version will release after this project is done.

#This Program utilizes the system terminal to download, sync, and install updates.
#If your terminal is blocked for security reasons. You may need to install updates manually.
#Please make sure git is installed. This script won't work without it.

#Import required moduels
from ast import arguments
import os #For file editing
import sys #Argmunent sending
import shutil #For folder deleting
import subprocess as sp
from custom_database import exit, clear, path #Used to close the app.

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
        UserInput=input('Remove the downloaded content: ')
        if UserInput==True:
            shutil.rmtree(
                "UpdateFolder"
            )
        #Exits the program and terminates the proccess.
        print("!Program will now terminate!")
        os._exit(1)
    print("Problems May Occur!")

#If all tests pass then let's install it! :)
if UpdateDatabase==True:
    #Saves the current version just incase if update fails as temp.py.
    os.rename('custom_database.py', 'temp.py')
    #Removed the current custom_database.py file.
    try:
        os.remove('custom_database.py')
    except:
        pass
    #Copys the new custom_database.py file.
    shutil.copyfile(
        path+'/UpdateFolder/database/custom_database.py',
        path+'/custom_database.py'
        )
    #If an error did occur revert back to old version.
    try:
        import custom_database
    except Exception as error:
        print('An Error Has Occured in the update proccess. Info is displayed below.')
        print(error)
        try:
            os.remove('custom_database.py')
        except:
            pass
        #Restores temp.py back to orginal name.
        os.rename('temp.py', 'custom_database.py')
    print("custom_database.py has been updated.")

if UpdateApplication==True:
    #Saves the current version just incase if update fails as temp.py.
    os.rename('app.py', 'temp.py')
    #Removed the current app.py file.
    try:
        os.remove('app.py')
    except:
        pass
    #Copys the new app.py file.
    shutil.copyfile(
        path+'/UpdateFolder/database/app.py',
        path+'/app.py'
        )
    #If an error did occur revert back to old version.
    try:
        sys.argv.append('--test')
        import app
    except Exception as error:
        print('An Error Has Occured in the update proccess. Info is displayed below.')
        print(error)
        try:
            os.remove('app.py')
        except:
            pass
        #Restores temp.py back to orginal name.
        os.rename('temp.py', 'app.py')
    print("app.py has been updated.")