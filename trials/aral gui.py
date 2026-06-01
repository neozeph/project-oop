from tkinter import *
from tkinter import messagebox
import sqlite3

def connect():
    conn=sqlite3.connect("../loginpage.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(name TEXT,username TEXT,password TEXT)")
    conn.commit()
    conn.close()
connect()

def viewallusers():
    conn=sqlite3.connect("../loginpage.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users")
    rows=cur.fetchall()
    conn.commit()
    conn.close()   
    return rows

def adduser(name,username,password):
    conn=sqlite3.connect("../loginpage.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO users VALUES(?,?,?)",(name,username,password))
    conn.commit()
    conn.close()

def deleteallusers():
    conn=sqlite3.connect("../loginpage.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    messagebox.showinfo('Successful', 'All users deleted')

def checkuser(username,password):
    conn=sqlite3.connect("../loginpage.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    result=cur.fetchone()
    return result

def getusername(username,password):
    conn=sqlite3.connect("../loginpage.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    result=cur.fetchone()
    global profilename
    if result!=None:
        profilename=result[0]

def viewwindow():
    gui = Toplevel(root)
    gui.title("VIEW ALL USERS")
    gui.geometry("800x700")
    Message(gui,font=("Castellar", 22, "bold"),text = "NAME      USERNAME      PASSWORD",width=700).pack()
    for row in viewallusers():
        a=row[0]
        b=row[1]
        c=""
        f=len(row[2])
        for i in range (f):
            c= c + "*"
        d = a + "         " + b + "           " + c
        Message(gui,fg='#6680ff',font=("adobe clean", 25, "bold"),text = d,width=700).pack()
    Button(gui,text="Exit Window",font=("candara",15,"bold"),activebackground="#fffa66",activeforeground="red",width=10,command=gui.destroy).pack()

def register():
    a = register_name.get()
    b = register_username.get()
    c = register_password.get()
    d = register_confpass.get()
    if c==d and c!="" and len(c)>5 and a!="" and b!="":
        adduser(a,b,c)
        messagebox.showinfo(':)', 'Registration Successful')      
    else :
        if(a=="" or b=="" or c=="" or d==""):
            messagebox.showinfo('Oops, Something went wrong', 'Field should not be empty')
        else:
            messagebox.showinfo('Oops, Something went wrong', 'Both passwords should be same! \nPassword should contain atleast 6 characters')
    reg_userentry.delete(0,END)
    reg_passentry.delete(0,END)
    reg_confpass.delete(0,END)
    reg_nameentry.delete(0,END)

def login():
    a = login_username.get()
    b = login_password.get() 
    getusername(a,b)   
    if (checkuser(a,b))!=None:
        messagebox.showinfo('Oops, Something went wrong', 'Testing lang')
        #root.destroy()
        #appwindow()     
    else:
        user_entry.delete(0,END)
        pass_entry.delete(0,END)
        messagebox.showinfo('Oops, Something went wrong', 'Invalid credentials')

profilename=""
t = 11

# Main code

root = Tk()
root.configure(bg='#D1FFF4')
root.title("CashWizz")
root.geometry("1000x700")
root.wm_attributes('-transparentcolor','grey')
rframe_photo = PhotoImage(file="Frame 1.png")
rframe_label = Label(root, border=0, bg = 'grey', image = rframe_photo)
rframe_label.pack(fill=BOTH)

#l3=Label(root,font=("arial black bold", 20), bg = "#8CEED7",fg = "white", text="Log in to your account").place(x=625,y=150)

# Login Button
login_btn = PhotoImage(file = "Log in.png")
login_image = Label(image = login_btn, text = "Log in")
login_button = Button(root, text="Register", font=("tahoma",19), command=login, image = login_btn, borderwidth=0, bg = "#8CEED7").place(x=550,y=395)

# Username
user_label = Label(root,font=("arial black", 12) ,text="Username:", bg = '#DCFAF3').place(x = 580, y = 248)
login_username=StringVar()
user_entry = Entry(root,width=27,border=0,font=('bold',11), textvariable=login_username,bg = '#DCFAF3')
user_entry.place(x=685, y=253)

# Password
pass_label = Label(root,font=("arial black",12) ,text="Password:", bg = '#DCFAF3').place(x = 580, y = 330)
login_password = StringVar()
pass_entry = Entry(root,width=27,border=0,font=('bold',11), textvariable=login_password, show="*", bg = '#DCFAF3')
pass_entry.place(x=685, y=335)

# Register
# Name ng user
reg_namelabel = Label(root,font=("arial black", 11) ,text="Name:", bg = '#DCFAF3').place(x = 75, y = 402)
register_name=StringVar()
reg_nameentry =Entry(root,width=27,border=0,font=('bold',11), textvariable=register_name,bg = '#DCFAF3') 
reg_nameentry.place(x = 140, y = 407)

# Username na gagamitin sa account
reg_userlabel = Label(root,font=("arial black", 11) ,text="Username:", bg = '#DCFAF3').place(x = 75, y = 440)
register_username=StringVar()
reg_userentry =Entry(root,width=27,border=0,font=('bold',11), textvariable=register_username ,bg = '#DCFAF3') 
reg_userentry.place(x = 175, y = 445)

# Password
reg_passlabel = Label(root,font=("arial black", 11) ,text="Password:", bg = '#DCFAF3').place(x = 75, y = 480)
register_password=StringVar()
reg_passentry =Entry(root,width=27,border=0,font=('bold',11), textvariable=register_password , bg = '#DCFAF3', show="*") 
reg_passentry.place(x=173,y=485)

# Password checker kung same
reg_passlabel = Label(root,font=("arial black", 11) ,text="Confirm Password:", bg = '#DCFAF3').place(x = 75, y = 520)
register_confpass=StringVar()
reg_confpass =Entry(root,width=20,border=0,font=('bold',11), textvariable=register_confpass , bg = '#DCFAF3', show="*") 
reg_confpass.place(x= 240,y=523)

# reg button
reg_btn = PhotoImage(file = "Group 1.png")
reg_image = Label(image = reg_btn)
reg_button = Button(root, font=("tahoma",19), command=register, image = reg_btn, borderwidth=0, bg = "#8CEED7").place(x=60,y=565)

# View accounts button
va_btn = PhotoImage(file = "Group 2.png")
va_image = Label(image = va_btn)
va_button = Button(root, font=("tahoma",19), command=viewwindow, image = va_btn, borderwidth=0, bg = "#8CEED7").place(x=255,y=565)

# Delete users button
del_btn = PhotoImage(file = "Del button.png")
del_image = Label(image = del_btn)
del_button = Button(root, font=("tahoma",19), command=deleteallusers, image = del_btn, borderwidth=0, bg = "#8CEED7").place(x=552,y=483)

root.resizable(False, False)
root.mainloop()



