from tkinter import *
from registerPopup import *
from backend import *

approot=Tk()
approot.title("User Management") # Sets the title of application

w=300 # width
h=200 # height
x=500 # x-position
y=250 # y-position
approot.geometry("%dx%d+%d+%d" %(w,h,x,y)) # Set the size of window application

approot.resizable(False, False) # Sets the window to unresizable

userDis=Label(approot,text="UserId/Email : ") # UserId/Email label text display
userDis.pack()
userDis.place(x=4,y=8)

userEntry=Entry(approot) # UserId/Email label text entry field
userEntry.pack()
userEntry.place(x=100,y=8)

passDis=Label(approot,text="Password : ") # Password label text display
passDis.pack()
passDis.place(x=4,y=40)

passEntry=Entry(approot) # Password label text entry field
passEntry.pack()
passEntry.place(x=100,y=40)

def sign_in_pushed():
    # function when the sign in button is pushed
    # get() is used to retrieve the text values
    user = userEntry.get()
    password = passEntry.get()

    access=sign_in(user,password)

    if access==True:
        print("Your access is granted!")
    else:
        print("\nUser Access Denied!")
        print("Wrong UserID/Email or Password entered....")


signInButton=Button(approot,text="Sign In",command=sign_in_pushed) # sign in button
signInButton.pack() # pack button to application root window
signInButton.place(x=180,y=70)

orLabel=Label(approot,text="(OR, You can Sign Up if you are not a user)")
orLabel.pack()
orLabel.place(x=35,y=120)

signUpButton=Button(approot,text="Sign Up",command=register_popup) # sign up button
signUpButton.pack() # pack button to application root window
signUpButton.place(x=120,y=155)

approot.mainloop() # Puts the application in a loop

