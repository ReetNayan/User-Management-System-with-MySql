from tkinter import *
from backend import *

def register_popup():
    win=Toplevel()
    win.title("Register In...")
    # Set the size and position of the pop-window
    w2 = 300  # width
    h2 = 200  # height
    x2 = 550  # x-position
    y2 = 300  # y-position
    win.geometry("%dx%d+%d+%d" % (w2, h2, x2, y2))
    win.resizable(False,False)

    name=Label(win,text="Name : ")
    name.pack()
    name.place(x=4,y=8)

    fnameDis=Label(win,text="First Name : ")
    fnameDis.pack()
    fnameDis.place(x=50,y=8)

    fnameEntry=Entry(win)
    fnameEntry.pack()
    fnameEntry.place(x=160,y=8)

    lnameDis=Label(win,text="Last Name :")
    lnameDis.pack()
    lnameDis.place(x=50,y=30)

    lnameEntry=Entry(win)
    lnameEntry.pack()
    lnameEntry.place(x=160,y=30)

    emailDis=Label(win,text="Email ID : ")
    emailDis.pack()
    emailDis.place(x=4,y=60)

    emailEntry=Entry(win)
    emailEntry.pack()
    emailEntry.place(x=70,y=60)

    userIDDis=Label(win,text="Unique User Name :")
    userIDDis.pack()
    userIDDis.place(x=4,y=90)

    userIDEntry=Entry(win)
    userIDEntry.pack()
    userIDEntry.place(x=130,y=90)

    maxChar=Label(win,text="(Maximum 4 Characters)")
    maxChar.pack()
    maxChar.place(x=130,y=105)

    passwordDis=Label(win,text="Password : ")
    passwordDis.pack()
    passwordDis.place(x=4,y=135)

    passwordEntry=Entry(win)
    passwordEntry.pack()
    passwordEntry.place(x=75,y=135)

    def register_pushed():
        f_name = fnameEntry.get()
        l_name = lnameEntry.get()
        email = emailEntry.get()
        userId = userIDEntry.get()
        password = passwordEntry.get()

        register_to_database(f_name,l_name,userId,email,password)

    register=Button(win,text="Register New Account",command=register_pushed)
    register.pack()
    register.place(x=90,y=160)
