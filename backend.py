import mysql.connector
import hasher
import randWord

database = mysql.connector.connect(host="host-address-of-mysql", user="mysql-username", passwd="mysql-password")

mycursor = database.cursor()

mycursor.execute("SHOW DATABASES LIKE 'UserManagementSystemDB' ;") # check if database already exists or not
getData=mycursor.fetchone() # fetch the returned data and store as a list
# if no database like this exists the list returned will be empty
if getData == None:
    #create database and table
    mycursor.execute("CREATE DATABASE UserManagementSystemDB ;")
    mycursor.execute("USE UserManagementSystemDB ;")
    mycursor.execute("CREATE TABLE accountdata (F_Name varchar(16), L_Name varchar(16), USERID varchar(4), EMAILID varchar(32), PSSWD_Hash varchar(64), Salt varchar(4)) ;")
else:
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
    if mycursor.fetchone()==None:  # checking if user exists in the database
        access=False
    else:
        command=""
        #if userID/Email is correct check for true password
        if len(user) <= 4:
            command = "SELECT F_Name, L_Name, PSSWD_Hash, Salt from accountdata WHERE USERID='" + user + "' ;"
        else:
            command = "SELECT F_Name, L_Name, PSSWD_Hash, Salt from accountdata WHERE EMAILID='" + user + "' ;"

        mycursor.execute(command)
        returnedData = mycursor.fetchone()  # returned data is stored as a list in respective manner
        # like this, returnedData = ('F_Name','L_Name','PSSWD_Hash','Salt')

        passwd_hash = returnedData[2]  # returned password hash is at index num 2 in returnedData
        hashof_psswd_entered = hasher.sha256(password, returnedData[3])  # returned salt is at index num 3 in returnedData
        
        # We hash the password entered with stored salt and compare it with original password hash
        if hashof_psswd_entered == passwd_hash:  # checking if stored password hash matches with the entered password hash
            access = True
            welcome(returnedData)  # print welcome message in which name of user is included
        else:
            access=False
    return access


def welcome(fetchedData):
    print("\nYou are "+fetchedData[0]+" "+fetchedData[1]+"! ")
    print("Welcome to your dashboard.")


def register_to_database(fname, lname, userid, email, passwd):

    # Now, we will retrieve the data from database based upon the
    # entered userid or email and compare with the existing data in database
    # if any of those are same user will have to enter any different thing from that.
    u = None
    e = None

    command = "SELECT USERID from accountdata WHERE USERID='"+userid+"' ;"
    mycursor.execute(command)
    returnedData1 = mycursor.fetchone()
    if returnedData1 == None:
        u = False
    else:
        u = True
    command = "SELECT EMAILID from accountdata WHERE EMAILID='"+email+"' ;"
    mycursor.execute(command)
    returnedData2 = mycursor.fetchone()
    if returnedData2 == None:
        e = False
    else:
        e = True

    if u is False and e is False:
        # Now, we check if email and user name are in
        # correct format or not. Then only we can insert
        # the data into the database.
        if len(userid) <= 4 and email.find('@') > 0:
            # We generate a random salt of 4 letters
            salt = randWord.genrt(4)

            # We now hash the password entered with given given salt and
            # store the hashed password alongwith salt
            password_hash = hasher.sha256(passwd, salt)

            values = (fname, lname, userid, email, password_hash, salt)
            insert_command = "INSERT INTO accountdata VALUES(%s,%s,%s,%s,%s,%s)"
            mycursor.execute(insert_command, values)
            database.commit()

            print("User Successfully registered!")
        else:
            print("Hmmm...either User ID or Email are entered in wrong format.")
            print("Please check those.")
    elif u is True and e is False :
        print("OOPS! Please choose a different User ID.")
    elif e is True and u is False:
        print("OOPS! Please choose a different Email.")
    elif e is True and u is True:
        print("OOPS! Please choose a different Email and User ID.")
    else:
        print("Some error occurred while registering you.")
        print("Please check if all things are entered correctly.")
