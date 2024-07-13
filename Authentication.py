# Authentication $ authorization
import tkinter.messagebox
from tkinter import *
import mysql.connector

db = mysql.connector.connect(host="localhost", username="root", password="", database="auth")
cursor = db.cursor()

def admin():
    global admin_frame, admin_username, admin_password
    admin_frame = Frame(root, width=350, height=200, bg='white')
    admin_frame.place(x=80, y=80)
    Label(admin_frame, text='Username', font=('georgia', 13, 'bold')).place(x=30, y=30)
    Label(admin_frame, text='Password', font=('georgia', 13, 'bold')).place(x=30, y=80)
    admin_username = StringVar()
    admin_password = StringVar()
    Entry(admin_frame, textvariable=admin_username, font=('georgia', 11), bg='lightblue').place(x=150, y=30)
    Entry(admin_frame, textvariable=admin_password, font=('georgia', 11), bg='lightblue', show='*').place(x=150, y=80)
    (Button(admin_frame, text="LOGIN", font=('georgia', 16, 'bold'), bg="lightblue", command=loginpage)
     .place(x=130, y=140))

def loginpage():
    username = admin_username.get()
    password = admin_password.get()
    cursor.execute("select * from detail where username = %s and password = %s", [username, password])
    data = cursor.fetchone()
    if data != None:
        tkinter.messagebox.showinfo("Authorization","Login Successfully")

    else:
        tkinter.messagebox.showinfo("Authorization", "Credentials not exist")



def user():
    global user_frame, Name, Mail, Gender, Username, Password
    user_frame = Frame(root, width=350, height=300, bg='white')
    user_frame.place(x=300, y=80)
    Label(user_frame, text="Name", font=('georgia', 13)).place(x=20, y=20)
    Label(user_frame, text="Mail", font=('georgia', 13)).place(x=20, y=60)
    Label(user_frame, text="Gender", font=('georgia', 13)).place(x=20, y=100)
    Label(user_frame, text="User Name", font=('georgia', 13)).place(x=20, y=140)
    Label(user_frame, text="Password", font=('georgia', 13)).place(x=20, y=180)
    Button(user_frame, text="signup", font=('georgia', 16), command=storedata).place(x=120, y=230)
    Name = StringVar()
    Mail = StringVar()
    Gender = StringVar()
    Username = StringVar()
    Password = StringVar()
    Entry(user_frame, textvariable=Name, font=('georgia', 13), width=20).place(x=120, y=20)
    Entry(user_frame, textvariable=Mail, font=('georgia', 13), width=20).place(x=120, y=60)
    (Radiobutton(user_frame, text="Male", variable=Gender, value='male',  font=('georgia', 11), bg="lightblue")
     .place(x=150, y=100))
    (Radiobutton(user_frame, text="Female", variable=Gender, value='female', font=('georgia', 11), bg="lightblue")
    .place(x=220, y=100))
    Entry(user_frame, textvariable=Username, font=('georgia', 13), width=20).place(x=120, y=140)
    Entry(user_frame, textvariable=Password, font=('georgia', 13), width=20).place(x=120, y=180)

def storedata():
    name = Name.get()
    mail = Mail.get()
    gender = Gender.get()
    username = Username.get()
    password = Password.get()
    cursor.execute("insert into detail(name, mail, gender, username, password) values(%s,%s,%s,%s,%s)",
                   [name, mail, gender, username, password])
    db.commit()
    tkinter.messagebox.showinfo("Authorization", "login successfully")


def login_page():
    global root
    root = Tk()
    root.geometry('700x700')
    root.title('Authentication')
    root.configure(bg="coral1")
    #Label
    Label(root, text='Login', font=('georgia',20), bg="white").place(x=330, y=10)
    #button
    Button(root, text="Admin", font=('georgia', 16), bg='white', command=admin).place(x=80, y=30)
    Button(root, text="User", font=('georgia', 16), bg='white', command=user).place(x=550, y=30)
    root.mainloop()

login_page()

db.close()


