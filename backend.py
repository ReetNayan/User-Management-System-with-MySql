import mysql.connector

database = mysql.connector.connect(host="<the hostname>", user="<mysql username>", passwd="<mysql password>")

mycursor = database.cursor()

mycursor.execute("SHOW DATABASES LIKE 'UserManagementSystemDB' ;") #check if database already exists or not
getData=mycursor.fetchone() #fetch the returned data and store as a list
#if no database like this exists the list returned will be empty
if len(getData)==0:
    #create database and table
    mycursor.execute("CREATE DATABASE UserManagementSystemDB ;")
    mycursor.execute("CREATE TABLE accountdata (F_Name varchar(16), L_Name varchar(16), USERID varchar(4), EMAILID varchar(32), PSSWD varchar(36)) ;")

mycursor.execute("USE UserManagementSystemDB ;")

def sign_in(user,password):
    access=None
    command=""
    #looking up for the entered user
    if len(user) <=4:
        command = "SELECT USERID from accountdata WHERE USERID='"+user+"' ;"
    else:
        command = "SELECT EMAILID from accountdata WHERE EMAILID='"+user+"' ;"
    mycursor.execute(command)
    if mycursor.fetchone()==None: # checking if user exists in the database
        access=False
    else:
        command=""
        #if userID/Email is correct check for true password
        if len(user) <= 4:
            command = "SELECT F_Name, L_Name, PSSWD from accountdata WHERE USERID='" + user + "' ;"
        else:
            command = "SELECT F_Name, L_Name, PSSWD from accountdata WHERE EMAILID='" + user + "' ;"
        mycursor.execute(command)
        returnedData=mycursor.fetchone()# returned data is stored as a list in respective manner
        # like this, returnedData = ('F_name','L_Name','PSSWD')
        if returnedData[2]==password: # checking if stored password matches with the entered
            access=True
            welcome(returnedData) # print welcome message in which name of user is included
        else:
            access=False
    return access

def welcome(fetchedData):
    print("\nYou are "+fetchedData[0]+" "+fetchedData[1]+"! ")

def register_to_database(fname,lname,userid,email,passwd):

    values=(fname,lname,userid,email,passwd)
    insertCmd="INSERT INTO accountdata VALUES(%s,%s,%s,%s,%s)"
    mycursor.execute(insertCmd,values)
    database.commit()

    print("User Successfully registered!")