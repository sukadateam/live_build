#Give a report of items not signed out, and items signed out. Not signed out on top. Signed out on bottom.
#Will be used to help the teacher see what may be missing.
from email.utils import parseaddr
from operator import truediv
from platform import python_version
from tkinter import *
from xml.etree.ElementTree import TreeBuilder
from custom_database import *
import subprocess
import webbrowser
import count
import time
tk= Tk()
tk.title('Carpetentry Application')
x='1920'
y='1080'
tk.geometry(x+"x"+y+"+10+20")
name=None
password=None
startup=True
other4=None
other5=None
other6=None
other7=None
other=None
other1=None
other2=None
other3=None #Encrypt/Decrypt Password
force=None
try:
    abdsdfugvyub=debug
except:
    print('Debug Var Not Found. Setting Debug To False.')
    debug=False
#If a button is called, it is displayed on the screen.
tk.attributes("-fullscreen")
def close_app_option():
    global other3
    if other3==None:
        exit()
    else:
        password1=other3
        safe_exit.close(create_backup=True, encryption_passw=password1, hide=logic.gate.not_gate(debug), random_name=True)
def version_note():
    global y
    e90=Label(tk, text='Program Version: '+program_version)
    e90.pack(side=BOTTOM, anchor=W)
class buttons:
    def show_users(y=100):
        e21 = Button(tk, text='Show Users', command=options.show_users, bg=button_color, foreground=text_color, font=text_font)
        e21.config(height=button_height, width=button_width)
        e21.place(x=((int(x))/2)-side_tilt, y=y)
    def center_buttons(y=100):
        e21 = Button(tk, text='Center Buttons', command=options.center_buttons, bg=button_color, foreground=text_color, font=text_font)
        e21.config(height=button_height, width=button_width)
        e21.place(x=((int(x))/2)-side_tilt, y=y)
    def credit(y=200):
        e20 = Button(tk, text='Credits', command=options.credits, bg=button_color, foreground=text_color, font=text_font)
        e20.config(height=button_height, width=button_width)
        e20.place(x=((int(x))/2)-side_tilt, y=y)
    def enable_debug(y=700):
        e18 = Button(tk, text='Enable Debug', command=options.enable_debug, bg=button_color, foreground=text_color, font=text_font)
        e18.config(height=button_height, width=button_width)
        e18.place(x=((int(x))/2)-side_tilt, y=y)
    def disable_debug(y=700):
        e19 = Button(tk, text='Disable Debug', command=options.disable_debug, bg=button_color, foreground=text_color, font=text_font)
        e19.config(height=button_height, width=button_width)
        e19.place(x=((int(x))/2)-side_tilt, y=y)
    def create_user(anchor=None, side=None):
        e1 = Button(tk, text='Create User', command=options.create_user, bg=button_color, foreground=text_color, font=text_font)
        e1.config(height=button_height, width=button_width)
        e1.place(x=((int(x))/2)-side_tilt, y=300)
    def remove_user(anchor=None, side=None):
        e2 = Button(tk, text='Remove User', command=options.remove_user, bg=button_color, foreground=text_color, font=text_font)
        e2.config(height=button_height, width=button_width)
        e2.place(x=((int(x))/2)-side_tilt, y=400)
    def change_password(anchor=None, side=None, y1=800):
        global x, y
        e3 = Button(tk, text='Change Password', command=options.create_password, bg=button_color, foreground=text_color, font=text_font)
        e3.config(height=button_height, width=button_width)
        e3.place(x=((int(x))/2)-side_tilt, y=y1)
    def logout(anchor=None, side=None, y=700):
        e4 = Button(tk, text='Logout', command=options.logout, bg=button_color, foreground=text_color, font=text_font)
        e4.config(height=button_height, width=button_width)
        e4.place(x=((int(x))/2)-side_tilt, y=y)
    def add_student(y=800):
        e14 = Button(tk, text='Add Student', command=options.add_student, bg=button_color, foreground=text_color, font=text_font)
        e14.config(height=button_height, width=button_width)
        e14.place(x=((int(x))/2)-side_tilt, y=y)
    def save(anchor=None, side=None):
        e5 = Button(tk, text='Save', command=options.save, bg=button_color, foreground=text_color, font=text_font)
        e5.config(height=button_height, width=button_width)
        e5.place(x=((int(x))/2)-side_tilt, y=500)
    def optimize(anchor=None, side=None):
        e6 = Button(tk, text='Optimize', command=options.optimize, bg=button_color, foreground=text_color, font=text_font)
        e6.config(height=button_height, width=button_width)
        e6.place(x=((int(x))/2)-side_tilt, y=600)
    def add_tool(anchor=None, side=None):
        e7 = Button(tk, text="Add Tool",command=options.add_tool, bg=button_color, foreground=text_color, font=text_font)
        e7.config(height=button_height, width=button_width)
        e7.place(x=((int(x))/2)-side_tilt, y=0)
    def remove_tool(anchor=None, side=None):
        e8 = Button(tk, text='Remove Tool', command=options.remove_tool, bg=button_color, foreground=text_color, font=text_font)
        e8.config(height=button_height, width=button_width)
        e8.place(x=((int(x))/2)-side_tilt, y=100)
    def show_tools(anchor=None, side=None):
        e9 = Button(tk, text='Show tools', command=options.show_tools, bg=button_color, foreground=text_color, font=text_font)
        e9.config(height=button_height, width=button_width)
        e9.place(x=((int(x))/2)-side_tilt, y=200)
    def clear_history(anchor=None, side=None):
        e10 = Button(tk, text='Clear History', command=options.clear_history, bg=button_color, foreground=text_color, font=text_font)
        e10.config(height=15, width=15)
        e10.place(x=0, y=0)
    def signout_item(anchor=None, side=None, y=100):
        e11 = Button(tk, text='Signout item', command=options.signout_item, bg=button_color, foreground=text_color, font=text_font)
        e11.config(height=button_height, width=button_width)
        e11.place(x=((int(x))/2)-side_tilt, y=y)
    def signin_item(anchor=None, side=None, y=0):
        e12 = Button(tk, text='Signin item', command=options.signin_item, bg=button_color, foreground=text_color, font=text_font)
        e12.config(height=button_height, width=button_width)
        e12.place(x=((int(x))/2)-side_tilt, y=y)
    def backup():
        e13 = Button(tk, text='Backup', command=options.backup, bg=button_color, foreground=text_color, font=text_font)
        e13.config(height=15, width=15)
        e13.pack(side=LEFT)
    def remove_student(y=900):
        e15 = Button(tk, text='Remove Student', command=options.remove_student, bg=button_color, foreground=text_color, font=text_font)
        e15.config(height=button_height, width=button_width)
        e15.place(x=((int(x))/2)-side_tilt, y=y)
    def show_logged_items(y=900):
        e16 = Button(tk, text='Show logged items', command=options.show_logged_items, bg=button_color, foreground=text_color, font=text_font)
        e16.config(height=button_height, width=button_width)
        e16.place(x=((int(x))/2)-side_tilt, y=y)
    def show_students(y=0):
        e17 = Button(tk, text='Show Students', command=options.show_students, bg=button_color, foreground=text_color, font=text_font)
        e17.config(height=button_height, width=button_width)
        e17.place(x=((int(x))/2)-side_tilt, y=y)
class options:
    def show_users():
        clear()
        e1 = Label(tk, text='Check Collections Folder For Info', bg=button_color, foreground=text_color)
        e1.config(height=button_height, width=button_width+10)
        e1.pack()
        e2 = Button(tk, text='Back', command=send, bg=button_color, foreground=text_color)
        e2.config(height=button_height, width=button_width)
        e2.pack()
        save_in_txtFile.users()
        os.chdir('collections')
        if systemDetectedOperatingSystem=="windows":
            os.system('notepad.exe users.txt')
        if systemDetectedOperatingSystem=="macos":
            subprocess.call(['open', '-a', 'TextEdit', 'users.txt'])
        os.chdir(path)
    def center_buttons(notInteger=False):
        global other2
        clear()
        e1=Label(tk, text='Change data_save file to permanently change.\nCurrent Value: '+str(side_tilt))
        e1.pack()
        other2=Entry(tk)
        other2.config(background=entry_background_color, fg=entry_text_color, width=button_width)
        other2.pack()
        e3=Button(tk, text='Submit', command=options.center_buttons_next)
        e3.pack()
        e2 = Button(tk, text='Back', command=send, bg=button_color, foreground=text_color)
        e2.config(height=button_height, width=button_width)
        e2.pack()
        if notInteger==True:
            e4=Label(tk, text='Please enter a number')
            e4.pack()
        Tk.update_idletasks(tk)
    def center_buttons_next():
        global other2, side_tilt
        try:
            side_tilt=int(other2.get())
            save.all(side_tiltForce=int(other2.get()))
            send()
        except ValueError:
            options.center_buttons(notInteger=True)
    def credits():
        clear()
        e1 = Label(tk, text='Created and Designed By Brandon Robinson\nPartial credit goes to Albert Plummer and Abdullahi Abdullahi\nGithub Page: github.com/sukadateam/database\nProgram Version: '+program_version, bg=button_color, foreground=text_color)
        e1.pack()
        e2 = Button(tk, text='Back', command=send, bg=button_color, foreground=text_color)
        e2.config(height=button_height, width=button_width)
        e2.pack()
        save_in_txtFile.students()
        Tk.update_idletasks(tk)
    def enable_debug():
        global debug
        debug=True
        send()
    def disable_debug():
        global debug
        debug=False
        send()
    def show_students():
        clear()
        e1 = Label(tk, text='Check Collections Folder For Info', bg=button_color, foreground=text_color)
        e1.config(height=button_height, width=button_width+10)
        e1.pack()
        e2 = Button(tk, text='Back', command=send, bg=button_color, foreground=text_color)
        e2.config(height=button_height, width=button_width)
        e2.pack()
        save_in_txtFile.students()
        os.chdir('collections')
        if systemDetectedOperatingSystem=="windows":
            os.system('notepad.exe student.txt')
        if systemDetectedOperatingSystem=="macos":
            subprocess.call(['open', '-a', 'TextEdit', 'student.txt'])
        os.chdir(path)
        Tk.update_idletasks(tk)
    def show_logged_items():
        clear()
        e1 = Label(tk, text='Check Collections Folder For Info', bg=button_color, foreground=text_color)
        e1.config(height=button_height, width=button_width+10)
        e1.pack()
        e2 = Button(tk, text='Back', command=send, bg=button_color, foreground=text_color)
        e2.config(height=button_height, width=button_width)
        e2.pack()
        save_in_txtFile.logs()
        os.chdir('collections')
        if systemDetectedOperatingSystem=="windows":
            os.system('notepad.exe student_logs.txt')
        if systemDetectedOperatingSystem=="macos":
            subprocess.call(['open', '-a', 'TextEdit', 'student_logs.txt'])
        os.chdir(path)
        Tk.update_idletasks(tk)
    def remove_student(notFound=False):
        clear()
        global other
        e1=Label(tk, text='Enter A Students Name to Remove')
        e1.pack()
        other=Entry(tk)
        other.pack()
        e3=Button(tk, text='Submit', command=options.remove_student_next)
        e3.pack()
        e4=Button(tk, text='Back', command=send)
        e4.pack()
        if notFound==True:
            e2=Label(tk, text='Student could not be found.')
            e2.pack()
        Tk.update_idletasks(tk)
    def remove_student_next():
        if other.get() in students:
            students.remove(other.get())
            send()
        else:
            options.remove_student(notFound=True)
    def add_student(student_found=False):
        clear()
        global other
        e3=Label(tk, text='New Students Name', bg=button_color, foreground=text_color)
        e3.pack()
        other=Entry(tk)
        other.config()
        other.pack()
        e1=Button(tk, text='Submit', command=options.add_student_next)
        e1.config(height=button_height, width=button_width)
        e1.pack()
        e5 = Button(tk, text='Back', command=send)
        e5.config(height=button_height, width=button_width)
        e5.pack()
        if student_found==True:
            e2=Label(tk, text='Student Exists.', bg=button_color, foreground=text_color)
            e2.pack()
        Tk.update_idletasks(tk)
    def add_student_next():
        global other
        if isinstance(other.get(), str) == True:
            if other.get() not in students:
                students.append(other.get())
                print('Student Added.')
                send()
            else:
                print('Student Exists.')
                options.add_student(student_found=True)
        else:
            print('Unknown Error.')
    def backup():
        global other3
        backup.create(random_name=True, password=other3, hide=logic.gate.not_gate(debug))
    def clear_history():
        history.clear()
    def show_tools():
        clear()
        e1 = Label(tk, text='Check Collections Folder For Info', bg=button_color, foreground=text_color)
        e1.config(height=button_height, width=button_width+10)
        e1.pack()
        e2 = Button(tk, text='Back', command=send, bg=button_color, foreground=text_color)
        e2.config(height=button_height, width=button_width)
        e2.pack()
        save_in_txtFile.tools()
        os.chdir('collections')
        if systemDetectedOperatingSystem=="windows":
            os.system('notepad.exe tools.txt')
        if systemDetectedOperatingSystem=="macos":
            subprocess.call(['open', '-a', 'TextEdit', 'tools.txt'])
        os.chdir(path)
        Tk.update_idletasks(tk)
    def signout_item(no_name=False, no_barcode=False, already_signed=False):
        global other, other1
        clear()
        e1 = Label(tk, text='Barcode/Serial', bg=button_color, foreground=text_color)
        e1.config(height=button_height, width=button_width)
        e1.pack()
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color, width=button_width)
        other.pack()
        e2 = Label(tk, text='Your Name', bg=button_color, foreground=text_color)
        e2.config(height=button_height, width=button_width)
        e2.pack()
        other1 = Entry(tk)
        other1.config(background=entry_background_color, fg=entry_text_color, width=button_width)
        other1.pack()
        e3 = Button(tk, text='Submit', command=options.signout_item_next, bg=button_color, foreground=text_color)
        e3.pack()
        e5 = Button(tk, text='Back', command=send, bg=button_color, foreground=text_color)
        e5.pack()
        if no_name==True:
            e6=Label(tk, text='Unknown Student', bg=button_color, foreground=text_color)
            e6.pack()
        if no_barcode==True:
            e7=Label(tk, text='Unknown Barcode/Serial', bg=button_color, foreground=text_color)
            e7.pack()
        if already_signed==True:
            e8=Label(tk, text='Item already signed out', bg=button_color, foreground=text_color)
            e8.pack()
        if secretsAllowed==True:
            secret.note()
        Tk.update_idletasks(tk)
    def signout_item_next():
        global other, other1
        list1=[other.get(), other1.get()]
        if check.barcode(str(list1[0]))==False and check.signed_out_item(str(list1[0]), hide=logic.gate.not_gate(debug))==False:
            if list1[1] in students or OnlyAllowKnownStudents==False:
                data_base.edit.add_item(data_base='logs', item_to_add=list1)
                clear()
                save.all(hide=logic.gate.not_gate(debug))
                send()
        else:
            name_no=False
            if list1[1] not in students and OnlyAllowKnownStudents==True:
                name_no=True
            options.signout_item(no_name=name_no, no_barcode=check.barcode(str(list1[0])), already_signed=check.signed_out_item(str(list1[0])))
    def signin_item(doesNotExist=False):
        global other
        clear()
        #Remove item by barcode Not name.
        e1 = Label(tk, text='Barcode/Serial', bg=button_color, foreground=text_color)
        e1.config(height=button_height, width=button_width)
        e1.pack()
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color, width=button_width)
        other.pack()
        e2 = Button(tk, text='Submit', command=options.signin_item_next, bg=button_color, foreground=text_color)
        e2.pack()
        e5 = Button(tk, text='Back', command=send, bg=button_color, foreground=text_color)
        e5.pack()
        if doesNotExist==True:
            e4=Label(tk, text='Item was not signed out\nAnd/Or Item does not exist', bg=button_color, foreground=text_color)
            e4.pack()
        Tk.update_idletasks(tk)
    def signin_item_next():
        global other
        if data_base.edit.app.remove_item(data_base='logs', barcode=other.get())==True:
            clear()
            save.all(hide=logic.gate.not_gate(debug))
            send()
        else:
            options.signin_item(doesNotExist=True)
    def remove_tool(toolDoesNotExist=False):
        global other
        clear()
        e1 = Label(tk, text='Barcode/Serial', bg=button_color, foreground=text_color)
        e1.pack()
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color)
        other.pack()
        e2 = Button(tk, text='Submit', command=options.remove_tool_next)
        e2.pack()
        e5 = Button(tk, text='Back', command=send)
        e5.pack()
        if toolDoesNotExist==True:
            e4=Label(tk, text='Tool Does Not Exist', bg=button_color, foreground=text_color)
            e4.pack()
        Tk.update_idletasks(tk)
    def remove_tool_next():
        global other
        name=other.get()
        if profanityFilter.filter(name)==0:
            if data_base.edit.app.remove_row(data_base='tools', name=name) == True:
                clear()
                send()
            else:
                options.remove_tool(toolDoesNotExist=True)
    def add_tool(id_exists=False):
        clear()
        global other, other1, other4, other5, other6, other7
        e10 = Label(tk, text='Tool Type', bg=button_color, foreground=text_color)
        e10.pack()
        other7 = Entry(tk)
        other7.config(background=entry_background_color, fg=entry_text_color)
        other7.pack()
        e1 = Label(tk, text='Tool Name', bg=button_color, foreground=text_color)
        e1.pack()
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color)
        other.pack()
        e2 = Label(tk, text='Barcode/Serial', bg=button_color, foreground=text_color)
        e2.pack()
        other1 = Entry(tk)
        other1.config(background=entry_background_color, fg=entry_text_color)
        other1.pack()
        e7 = Label(tk, text='Model Number', bg=button_color, foreground=text_color)
        e7.pack()
        other4 = Entry(tk)
        other4.config(background=entry_background_color, fg=entry_text_color)
        other4.pack()
        e8 = Label(tk, text='Purchase Date', bg=button_color, foreground=text_color)
        e8.pack()
        other5 = Entry(tk)
        other5.config(background=entry_background_color, fg=entry_text_color)
        other5.pack()
        e9 = Label(tk, text='Loaned To', bg=button_color, foreground=text_color)
        e9.pack()
        other6 = Entry(tk)
        other6.config(background=entry_background_color, fg=entry_text_color)
        other6.pack()
        e3 = Button(tk, text='Submit', command=options.add_tool_next)
        e3.pack()
        e5 = Button(tk, text='Back', command=send)
        e5.pack()
        if id_exists==True:
            e6=Label(tk, text='Barcode/Serial Exists', bg=button_color, foreground=text_color)
            e6.pack()
        Tk.update_idletasks(tk)
    def add_tool_next(replace=''):
        global other, other1, other4, other5, other6, other7
        name = other.get()
        id = other1.get()
        modelNumber=other4.get()
        purchaseDate=other5.get()
        loandedTo=other6.get()
        toolType=other7.get()
        if modelNumber in [None, '', ' ', '  ']:
            modelNumber=replace
        if purchaseDate in [None, '', ' ', '  ']:
            purchaseDate=replace
        if loandedTo in [None, '', ' ', '  ']:
            loandedTo=replace
        if toolType in [None, '', ' ', '  ']:
            toolType=replace
        if check.barcode(id)==True:
            if profanityFilter.filter(name)==0 and profanityFilter.filter(id)==0:
                data_base.edit.add_row(data_base='tools', new_row=[str(toolType), str(name),str(id), str(modelNumber), str(purchaseDate), str(loandedTo)], split=False)
            if printer_debug==True:
                print('Creating Barcode...')
            print_instructions.createBarcode(id, qr_code=True)
            if printer_debug==True:
                print('Printing...')
            print_instructions.print('barcode.png')
            clear()
            send()
        else:
            options.add_tool(id_exists=True)
    def create_password():
        global other
        clear()
        e1 = Label(tk, text='New password', bg=button_color, foreground=text_color)
        e1.pack()
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color)
        other.pack()
        e3 = Button(tk, text='Submit',command=options.create_password_next)
        e3.pack()
        e5 = Button(tk, text='Back', command=send)
        e5.pack()
        Tk.update_idletasks(tk)
    def create_password_next():
        global other
        passw=other.get()
        get.new_hash(passw=passw, normal=True)
        send()
    def logout():
        users.logout()
        clear()
        login()
    def create_user(user_exists=False, unknownPermission=False, PasswordDoesNotMeetReq=False, NoUsernameEntered=False, InvalidPassword=False):
        clear()
        global other, other1, other2
        e1 = Label(tk, text='New user', bg=button_color, foreground=text_color)
        e1.pack()
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color)
        other.pack()
        e2 = Label(tk, text='Password', bg=button_color, foreground=text_color)
        e2.pack()
        other1 = Entry(tk)
        other1.config(background=entry_background_color, fg=entry_text_color)
        other1.pack() 
        e3 = Label(tk, text='Permission', bg=button_color, foreground=text_color)
        e3.pack()
        other2 = Entry(tk)
        other2.config(background=entry_background_color, fg=entry_text_color)
        other2.pack()
        e4 = Button(tk, text='Submit', command=options.create_user_next)
        e4.pack()
        e5 = Button(tk, text='Back', command=send)
        e5.pack()
        if user_exists==True:
            e6=Label(tk, text='User exists', bg=button_color, foreground=text_color)
            e6.pack()
        if unknownPermission==True:
            e7=Label(tk, text='Unknown Permission\nAllowed Permissions:\nAdmin, Teacher, Student', bg=button_color, foreground=text_color)
            e7.pack()
        if PasswordDoesNotMeetReq==True:
            e8=Label(tk, text='Password Does Not Meet Requirements\nMin Length:'+str(min_length)+'\nMax Length: '+str(max_length)+'\nAllowed Characters: '+allowedPassword_chars, bg=button_color, foreground=text_color)
            e8.pack()
        if NoUsernameEntered==True:
            e9=Label(tk, text='Give the user a name', bg=button_color, foreground=text_color)
            e9.pack()
        if InvalidPassword==True:
            e10=Label(tk, text='Invalid Password', bg=button_color, foreground=text_color)
            e10.pack()
        Tk.update_idletasks(tk)
    def create_user_next():
        global other, other1, other2
        name=other.get()
        password=other1.get()
        permission=other2.get()
        if name in [None, '', ' ', '  ']:
            options.create_user(NoUsernameEntered=True)
        elif password in [None, '', ' ', '  ']:
            options.create_user(InvalidPassword=True)
        else:
            if profanityFilter.filter(name)==0 and profanityFilter.filter(password)==0 and profanityFilter.filter(permission)==0:
                if users.create(new_user=name.lower(), new_password=password, new_permission=permission.lower())==False:
                    options.create_user(user_exists=True)
                elif users.create(new_user=name.lower(), new_password=password, new_permission=permission.lower())=="IncorrectPerm":
                    options.create_user(unknownPermission=True)
                elif users.create(new_user=name.lower(), new_password=password, new_permission=permission.lower())=="PasswordDoesNotMeetReq":
                    options.create_user(PasswordDoesNotMeetReq=True)
                else:
                    other, other1, other2 = None, None, None
                    send()
        Tk.update_idletasks(tk)
    def remove_user(UserNotFound=False, ThatsYou=False):
        clear()
        e1 = Label(tk, text='User')
        e1.pack()
        global other
        other = Entry(tk)
        other.config(background=entry_background_color, fg=entry_text_color)
        other.pack()
        e2 = Button(tk, text='Submit', command=options.remove_user_next)
        e2.pack()
        e5 = Button(tk, text='Back', command=send)
        e5.pack()
        if ThatsYou==True:
            e7=Label(tk, text='Wait! That was you. I cannot get rid of you.\nI need you here.', bg=button_color, foreground=text_color)
            e7.pack()
        if UserNotFound==True:
            e6=Label(tk, text='User Does Not Exist', bg=button_color, foreground=text_color)
            e6.pack()
        Tk.update_idletasks(tk)
    def remove_user_next():
        global other
        user=other.get()
        user1, permission=users.return_login_cred()
        if user1==user.lower():
            options.remove_user(ThatsYou=True)
        elif str(user.lower()) in [None, '', ' ', '  ']:
            options.remove_user(UserNotFound=True)
        else:
            if user1.lower() != user.lower() and profanityFilter.filter(user.lower())==0:
                if users.remove(user=str(user.lower()))=="UserNotFound":
                    options.remove_user(UserNotFound=True)
                else:
                    clear()
                    send()
            else:
                clear()
                send()
    def save():
        save.all(hide=logic.gate.not_gate(debug))
    def optimize():
        optimize.run(save_optimizations=True, hide=logic.gate.not_gate(debug))
        clear()
        login()
#Call to clear the screen.
def clear():
    for widget in tk.winfo_children():
        widget.destroy()
#Sends logged in users to correct area depending on permissions.
def send():
    global force
    try: os.remove('data_save.aes')
    except: pass
    try: os.remove('history.aes')
    except: pass
    save.all(hide=logic.gate.not_gate(debug))
    try:
        os.remove('hash.txt')
    except:
        pass
    try:
        name, perm= users.return_login_cred()
    except:
        pass
    if force!=None:
       perm=force
    if perm=="secret":
        secret_screen()
    if perm == "admin":
        admin_screen()
    if perm == "teacher":
        teacher_screen()
    if perm == "student":
        student_screen()
def secret_screen():
    clear()
    e1=Label(tk, text='Wow. You found the 4th secret! One more to go!')
    e1.pack()
    buttons.logout(y=100)
class secret:
    def note():
        e51=Label(tk, text='<secret>\nPATHS')
        e51.pack(anchor=SW, side=RIGHT)
    def save_answer(question, answer):
        try:
            file=open('answers.txt','a')
        except:
            file=open('answers.txt','w')
        file.write('Question: '+display.space(question, max_length=35)+'  Answer: '+display.space(answer, max_length=35)+'\n')
        file.close()
    def random():
        #Question, Button1, Button2
        list15=[['Oh no, our table it\'s broken! What should we do?','Go to Ikea. :(','Use some duct tape!'],['Is english hard?','Engrish','No. It\'s easy.'],['Potato + Squash = ?','Squatato','Watermelon'],['What\'s funnier than 24?','25','23'],['Are you human?','Yes','No'],['Do you like this app?','Yes, It\'s perfect!','No, it could be better.'],['Are taco bell bathrooms clean?','Yes','Oh hell nay!'],['Have you heard of Linus Tech Tips?','Yes','No'],['Who is the first President of the United States?','John Adams','George Washington'],['Do you like memes?','Yes','No'],['Do you like video games?','Yes','No'],['Are you a good person?','Yes','No'],['Who lives in a pineapple under the sea?','Patrick','Spongebob'],['What does Mr. Krabs like the most?','Money','Krappy Patty Formula'],['Chief Wiggims is from what show?','American Dad','Family Guy'],['Peter Griffion is from what show?','American Dad','Family Guy'],['Sally has 10 hotdogs. She ate 5 of them.\nHow many are left?','5','10'],['Dogs Or Cats?','Dogs','Cats'],['Sara would like to send you a picture.','Yes Please!','No thanks.'],['Marvel or DC?','Marvel','DC'],['Click the Yes button.','No','Yes'],['1+1=','2','3'],['Life Or Death?','Life','Death'],['Click No','No','Yes'],['Apple or Samsung?','Apple','Samsung'],['Gem rush your town hall? (COC)','Yes','No! Don\'t waste your gems!'],['Are you an American?','Yes','No'],['Are you a Lefty or Righty?','Righty','Lefty'],['59+125=','184','187'],['Can I get a hiyah?!','Hiyah!','I\'m not a little kid'], ['Do you like PATHS?', 'Yes', 'No'], ['Do you agree?', 'Yes', 'No'], ['What color is blue?','Red','Blue'], ['Is the earth flat?','Yes','No'], ['Does Ohio exist?','Yes','No'], ['Is water wet?','Yes','No'], ['Time for Crab.','Rate','Close'], ['2+2=','21','4.01'], ['Who lives in a pinapple under the sea?','Squidward','SpongQuan'], ['Why are you gay?','What?','Who said i\'m gay?'], ['Fries or Onion rings?','Yes','No'], ['Do you support raccoon rights?','Yes','Yes'], ['Is proper grammar important in an online setting','n0p3','Yes, it is'], ['Do all your base belong to us?','Yes','No'], ['Waffles or Pancakes','Waffles','Pancakes'], ['Badger Badger Badger Badger Badger Badger','Mushroom','Mushroom'], ['You werent supposed to see this get out','Leave','Leave'],['Your teammate has initiated a surrender','F1 Surrender','F2 Continue'], ['Ninjas or Pirates','Ninjas','Pirates'], ['Bulbasaur,Charmander or Squirtle','Charmander','Squirtle'], ['Heads or Tails','Heads','Tails'], ['Is the washington post a reliable source of news','No','Yes'], ['Eat the rich?','Yes','Yes'], ['Is dirt dirty','Yes','No'], ['What\'s brown and sticky','A stick','*redacted*'], ['Soup or Salad?','soup','WHATS A SUPERSALAD'], ['Up or down?','dowp','upown'], ['Is this statement true?','True','False'], ['Could we cover the earth in pudding?','Maybe','Hmmmm Pudding!'],['Are we real?','Yes','Mayonaise'],['Is mayonaise an instrament?','Pudding','Horseraddish'],['Do you like your teacher?','Yes','No'], ['Which do you like more?', 'Tacos', 'Salad']]
        item=random.randint(0, len(list15)-1)
        return (list15[item])[0], (list15[item])[1], (list15[item])[2]
    def item1():
        e50=Button(tk, text='PATHS', command=secret.item1_next)
        e50.pack(anchor=NW)
    def item1_next():
        global other1, other2, other
        clear()
        other, other1, other2=secret.random()
        e1=Label(tk, text=other)
        e1.pack(anchor=N)
        button3=Button(tk, text=other1, command=secret.button3)
        button3.pack(anchor=N)
        button4=Button(tk, text=other2, command=secret.button4)
        button4.pack(anchor=N)
    def button3():
        global other, other1
        secret.save_answer(question=other, answer=other1)
        send()
    def button4():
        global other, other2
        secret.save_answer(question=other, answer=other2)
        send()
#If permission is student
def student_screen():
    clear()
    buttons.signout_item()
    buttons.signin_item()
    buttons.credit()
    buttons.logout(y=300)
    secret.item1()
    version_note()
#If permission is teacher. First page.
def teacher_screen():
    global other3
    clear()
    version_note()
    buttons.add_tool()
    buttons.remove_tool()
    buttons.show_tools()
    buttons.create_user()
    buttons.remove_user()
    if OnlyAllowKnownStudents==True:
        buttons.show_students(y=500)
        buttons.add_student(y=600)
        buttons.remove_student(y=700)
        e25=Button(tk, text='Next Screen', command=teacher_page2, bg=button_color, foreground=text_color, font=text_font)
        e25.config(height=button_height, width=button_width)
        e25.place(x=((int(x))/2)-side_tilt, y=800)
    else:
        e25=Button(tk, text='Next Screen', command=teacher_page2, bg=button_color, foreground=text_color, font=text_font)
        e25.config(height=button_height, width=button_width)
        e25.place(x=((int(x))/2)-side_tilt, y=500)
#Teacher second page.
def teacher_page2():
    clear()
    version_note()
    buttons.show_logged_items(y=0)
    buttons.logout(y=100)
    e25=Button(tk, text='Back', command=teacher_screen, bg=button_color, foreground=text_color, font=text_font)
    e25.config(height=button_height, width=button_width)
    e25.place(x=((int(x))/2)-side_tilt, y=200)
#If permission is admin. First page.
def admin_screen():
    clear()
    version_note()
    buttons.add_tool()
    buttons.remove_tool()
    buttons.show_tools()
    buttons.create_user()
    buttons.remove_user()
    buttons.save()
    buttons.optimize()
    buttons.clear_history()
    buttons.backup()
    if debug==True:
        buttons.disable_debug(y=700)
    else:
        buttons.enable_debug(y=700)
    e25=Button(tk, text='Next Screen', command=admin_page2, bg=button_color, foreground=text_color, font=text_font)
    e25.config(height=button_height, width=button_width)
    e25.place(x=((int(x))/2)-side_tilt, y=800)
#Admin second page
def admin_page2():
    clear()
    version_note()
    buttons.logout(y=0)
    buttons.signin_item(y=100)
    buttons.signout_item(y=200)
    buttons.show_logged_items(y=300)
    buttons.show_students(y=400)
    buttons.change_password(y1=500)
    buttons.center_buttons(y=600)
    buttons.show_users(y=700)
    e25=Button(tk, text='Back', command=admin_screen, bg=button_color, foreground=text_color, font=text_font)
    e25.config(height=button_height, width=button_width)
    e25.place(x=((int(x))/2)-side_tilt, y=800)
#Ask the database if the entered credentials are correct.
def ask(command=send):
    global name, password, startup
    try:
        user=name.get()
        pass_w=password.get()
        s=True
    except:
        s=True
        login()
    if secretsAllowed==True:
        if user=="<turtles>":
            if pass_w=="forever":
                clear()
                e1=Label(tk, text='Congrats you found (a) secret page. Try and find more! (2/5)\nHint: A button is not what it seems.')
                e1.pack()
                e2=Button(tk, text='Back', command=login)
                e2.pack()
                s=False
        if user=="<secret>":
            if pass_w=="PATHS":
                clear()
                e1=Label(tk, text='Congrats you found (a) secret page. Try and find more! (1/5)\n<turtles> should live forever')
                e1.pack()
                e2=Button(tk, text='Back', command=login)
                e2.pack()
                s=False
    if s==True:
        if users.login_request(user=user.lower(), password=pass_w) == True:
            if profanityFilter.filter(str(name))==0 and profanityFilter.filter(str(pass_w))==0:
                print('Login Success!')
                u, p = users.return_login_cred()
                if p == "admin" or p=="teacher":
                    if startup==True:
                        ask_encrypt_password()
                    else:
                        command()
                else:
                    command()
            else:
                command()
        else:
            clear()
            print('Incorrect Password Attempt')
            history.create_history(user=user, usage='Login Failed', add_desc=True, desc='Incorrect Password', manual_record=True, hide=logic.gate.not_gate(debug))
            login(wrong=True)
#Ask for the encyption password to allow for auto backups.
def ask_encrypt_password(wrong=False): 
    if os.path.exists('hash.aes')==1:
        global other3
        clear()
        version_note()
        e1=Label(tk, text='Enter Encrypt/Decrypt Password', width=23)
        e1.pack()
        other3=Entry(tk, show='*')
        other3.config(background=entry_background_color, fg=entry_text_color)
        other3.pack()
        e3=Button(tk, text='Submit', command=ask_encrypt_password_next)
        e3.pack()
        e5=Button(tk, text='Back', command=options.logout)
        e5.pack()
        if wrong==True:
            e4=Label(tk, text='Incorrect Password', width=20)
            e4.pack()
        Tk.update_idletasks(tk)
    else:
        print('Could not find hash. Asking user to create one.')
        clear()
        create_encryption_password()
def ask_encrypt_password_next():
    global other3, startup
    other3=other3.get()
    clear()
    if check.encyption_password(other3) == 0:
        startup=False
        send()
    else:
        history.create_history('Unknown User', 'Incorrect Encryption Password', manual_record=True, hide=logic.gate.not_gate(debug))
        ask_encrypt_password(wrong=True)
    Tk.update_idletasks(tk)
#Display a screen that allows the user to login.
def login(wrong=False, e1_button='Login', command=ask, show_student_button=True, show_exit_button=True):
    clear()
    version_note()
    global name, password, force
    force=None
    e2 = Label(tk, text='Username: ')
    e2.pack()
    name = Entry(tk, highlightbackground='Black')
    name.config(background=entry_background_color, fg=entry_text_color)
    name.pack()
    e4 = Label(tk, text='Password: ')
    e4.pack()
    password = Entry(tk, show='*')
    password.config(background=entry_background_color, fg=entry_text_color, highlightbackground='Black')
    password.pack()
    e1 = Button(tk, text=e1_button, command=command, bg=button_color, foreground=text_color, font=text_font)
    e1.config(height=1, width=7)
    e1.pack()
    if show_exit_button==True:
        e5 = Button(tk, text='Exit', command=close_app_option, width=20, bg=button_color, foreground=text_color, font=text_font)
        e5.config(height=1, width=button_width)
        e5.config(width=7)
        e5.pack()
    if show_student_button==True:
        e7=Button(tk, text='Student', command=force_student, width=20, bg=button_color, foreground=text_color, font=text_font)
        e7.config(height=1, width=7)
        e7.pack()
    if wrong==True:
        e6=Label(tk, text='Incorrect Password', width=20)
        e6.pack()
    Tk.update_idletasks(tk)
    Tk.update(tk)
#Force the student page.
def force_student():
    global user_permission, user_logged, force
    user_logged='student'
    user_permission='student'
    force='student'
    send()
#Exit application
def exit_app():
    global other
    clear()
    e1 = Label(tk, text='Password')
    e1.pack()
    other = Entry(tk, show='*')
    other.config(background=entry_background_color, fg=entry_text_color)
    other.pack()
    e3 = Button(tk, text='Submit',command=exit_app_next)
    e3.pack()
    e4 = Button(tk, text='Back', command=login)
    e4.pack()
    Tk.update_idletasks(tk)
def exit_app_next():
    global other
    pass_w=other.get()
    if encrypt.all(password=pass_w) == 1:
        clear()
        login()
    else:
        exit()
#Decrypt app
def open_app():
    global other
    clear()
    e1 = Label(tk, text='Password')
    e1.pack()
    other = Entry(tk, show='*')
    other.config(background=entry_background_color, fg=entry_text_color)
    other.pack()
    e3 = Button(tk, text='Submit', command=open_app_next)
    e3.pack()
def open_app_next():
    global other
    pass_w=other.get()
    if decrypt.all(password=pass_w) == 1:
        clear()
        open_app()
    else:
        clear()
        exit()
#If encryption password(s) don't exist, ask them to make one.
def create_encryption_password(InvalidPassword=False):
    version_note()
    global other3
    e1=Label(tk, text='Enter new Encryption Password', width=22)
    e1.pack()
    other3=Entry(tk)
    other3.config(background=entry_background_color, fg=entry_text_color)
    other3.pack()
    e2=Button(tk, text='Submit', command=create_encryption_password_next)
    e2.pack()
    if InvalidPassword==True:
        e3=Label(tk, text='Invalid Password')
        e3.pack()
    Tk.update_idletasks(tk)
def create_encryption_password_next():
    global other3, startup
    if str(other3.get()) in [None, '', ' ','  ']:
        print('Got it')
        clear()
        create_encryption_password(InvalidPassword=True)
    else:
        try:
            get.new_hash(normal=True, passw=str(other3.get()), memory_float=True) #Makes a new hash
            startup=False
            send()
        except:
            print("Something happened in create_encryption_password")
            clear()
            try:
                os.remove('hash.txt')
            except:
                pass
            create_encryption_password()
tk.config(bg=bg_color)
#Check if the save file is encrypted. If so, ask user for the decrypt password.
if os.path.exists('history.aes')==True or os.path.exists('data_save.aes'):
    open_app()
else:
    login()
tk.mainloop()