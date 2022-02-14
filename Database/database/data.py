data_bases=[['tools', True, 'all', 'column_row', ['name','id']], ['logs', True, 'all', 'list']]
#Name, Active status, owner, type, columns(if type == column_row)
row=[]
#Side to side
#Data_base, items in row
lists=[]
#Lists
#Data_base, items in list

#Authentication
known_users=['admin', 'teacher']
passwords=['admin', 'teacher']
#Look at line 24 for allowed permissions. allowed_users=[]
permissions=['admin', 'teacher']
#True = Enabled, False = Disabled.
active_users=[True, True]

#Current user logged in
user_logged=None
user_permission=None

#Others
allowed_types=['column_row', 'list']
allowed_users=['admin', 'student', 'teacher', 'secret'] #Allowed Permissions
denied_inputs=['',' ',None]
denied_names=[]
debug=True
students=[]
opto_data=[]
opto_row=[]
opto_lists=[]
side_tilt=200