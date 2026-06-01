import time
import sqlite3
from tkinter import *
from tkinter import messagebox

def connect():
    conn = sqlite3.connect("loginpage.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(name TEXT,username TEXT,password TEXT)")
    conn.commit()
    conn.close()

connect()

def viewAllUsers():
    conn = sqlite3.connect("loginpage.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def viewAllUsers2():
    listA.insert(END, "NAME")
    listB.insert(END, "USERNAME")
    listC.insert(END, "PASSWORD")
    for row in viewAllUsers():
        a, b, c = map(str, row)
        hidden_password = "*" * len(c)

        listA.insert(END, a)
        listB.insert(END, b)
        listC.insert(END, hidden_password)

def addUser(name, username, password):
    conn = sqlite3.connect("loginpage.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES(?,?,?)", (name, username, password))
    conn.commit()
    conn.close()

def deleteAllUsers():
    conn = sqlite3.connect("loginpage.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    messagebox.showinfo('Successful', 'All users deleted')

def checkUser(username, password):
    conn = sqlite3.connect("loginpage.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cur.fetchone()
    return result

def getusername(username, password):
    conn = sqlite3.connect("loginpage.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cur.fetchone()
    global profilename
    if result != None:
        profilename = result[0]

def viewwindow():
    global listA, listB, listC
    gui = Toplevel(root)
    gui.title("CashWizz")
    gui.geometry("800x700")
    gui.wm_attributes('-transparentcolor', 'grey')

    userLblImg = Label(gui, border=0, bg='grey', image=userTable_photo)
    userLblImg.pack(fill=BOTH)

    listA = Listbox(gui, width=15, height=10, font=("century", 20), justify="center", bg="#DCFAF3")
    listB = Listbox(gui, width=15, height=10, font=("century", 20), justify="center", bg="#DCFAF3")
    listC = Listbox(gui, width=13, height=10, font=("century", 20), justify="center", bg="#DCFAF3")

    viewAllUsers2()
    listA.place(x=30, y=200)
    listB.place(x=280, y=200)
    listC.place(x=540, y=200)

    gui.resizable(False, False)
    gui.mainloop()

def register():
    a = register_name.get()
    b = register_username.get()
    c = register_password.get()
    d = register_confpass.get()
    if c == d and c != "" and len(c) > 5 and a != "" and b != "":
        addUser(a, b, c)
        messagebox.showinfo('CashWizz', 'Registration Successful')
    else:
        if (a == "" or b == "" or c == "" or d == ""):
            messagebox.showerror('Error', 'Field should not be empty')
        else:
            messagebox.showerror('Error',
                                'Both passwords should be same! \nPassword should contain atleast 6 characters')
    reg_userentry.delete(0, END)
    reg_passentry.delete(0, END)
    reg_confpass.delete(0, END)
    reg_nameentry.delete(0, END)

def login():
    a = login_username.get()
    b = login_password.get()
    getusername(a, b)
    if (checkUser(a, b)) != None:
        root.destroy()
        appWindow()
    else:
        user_entry.delete(0, END)
        pass_entry.delete(0, END)
        messagebox.showerror('Error', 'Invalid credentials')

profilename = ""
t = 10

def appWindow():
    def connect1():
        conn = sqlite3.connect("expenseapp.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS expensetable(id INTEGER PRIMARY KEY,itemname TEXT,date TEXT,cost TEXT,category TEXT)")
        conn.commit()
        conn.close()

    connect1()

    def insert(itemname, date, cost, category):
        conn = sqlite3.connect("expenseapp.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO expensetable (itemname, date, cost, category) VALUES(?,?,?,?)", (itemname, date, cost, category))
        conn.commit()
        conn.close()

    def view():
        conn = sqlite3.connect("expenseapp.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM expensetable")
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows

    # To search item (includes sqlite3)
    def search(itemname="", date="", cost="", category=""):
        conn = sqlite3.connect("expenseapp.db")
        cur = conn.cursor()
        cur.execute("SELECT *FROM expensetable WHERE itemname=? OR date=? OR cost=? OR category=?", (itemname, date, cost, category))
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows

    def delete(id):
        conn = sqlite3.connect("expenseapp.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM expensetable WHERE id=?", (id))
        conn.commit()
        conn.close()

    def deletealldata():
        conn = sqlite3.connect("expenseapp.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM expensetable")
        conn.commit()
        conn.close()
        messagebox.showinfo('Successful', 'All data deleted')

    def sumofitems():
        global a,b,c
        conn = sqlite3.connect("expenseapp.db")
        cur = conn.cursor()
        cur.execute("SELECT SUM(cost) FROM expensetable")
        sum = cur.fetchone()
        if sum[0] is None:
            messagebox.showinfo("Error", "There are no expenses made yet.")
            a = "YOU SPENT NOTHING YET"
            c = "Spend some money!"
        else:
            b = str(sum[0])
            d = "Php " + str(round(float(sum[0]),2))
            a = "YOU SPENT " + d

            if int(b) <= 1000:
                c = "You're spending wisely."
            elif int(b) > 1000 and int(b) <= 5000:
                c = "Oops! Be mindful of spending."
            elif int(b) > 5000 and int(b) <= 10000:
                c = "OMG! You're a spendthrift!"
            else:
                c = "WOW! So expensive."
            conn.commit()
            conn.close()
            return sum,a,b,c

    def expensesTableGUI():
        global list1
        expTable = Toplevel(gui)
        expTable.title("CashWizz Expenses Table")
        expTable.geometry("1000x700")
        expTable.wm_attributes('-transparentcolor', 'grey')
        expTablePhoto = PhotoImage(file="images/ExpTable.png")
        expTableLabel = Label(expTable, border=0, bg='grey', image=expTablePhoto)
        expTableLabel.pack(fill=BOTH)

        scroll_bar = Scrollbar(expTable)
        scroll_bar.place(x=870, y=170, height=416, width=25)
        list1 = Listbox(expTable, width=50, height=12,  font=("century", 20), yscrollcommand=scroll_bar.set, bg="#DCFAF3")
        viewallitems()
        list1.place(x=120, y=170)
        scroll_bar.config(command=list1.yview)

        expTable.resizable(False, False)
        expTable.mainloop()
        expTable.mainloop()

    def totalExpenses():
        expttl = Toplevel(gui)
        expttl.title("CashWizz Expenses")
        expttl.geometry("500x400")
        expttl.wm_attributes('-transparentcolor', 'grey')
        expPhoto = PhotoImage(file="images/TotalExpense.png")
        expLabel = Label(expttl, border=0, bg='grey', image=expPhoto)
        expLabel.pack(fill=BOTH)

        sumofitems()
        Label(expttl, text=a, font="Helvetica 20 bold", bg="#DCFAF3").place(relx=.5, rely=.5, anchor=CENTER)
        Label(expttl, text=c, font="Helvetica 14", bg="#DCFAF3").place(relx=.5, rely=.7, anchor=CENTER)

        expttl.resizable(False, False)
        expttl.mainloop()

    def insertitems():
        a = exp_itemname.get()
        b = exp_date.get()
        c = exp_cost.get()
        f = exp_categ.get()
        d = c.replace('.', '', 1)
        e = b.count('-')

        if a == "" or b == "" or c == "" or f == "":
            messagebox.showinfo("Error", "Field should not be empty")
        elif len(b) != 10 or e != 2:
            messagebox.showinfo("Error", "DATE should be in format dd-mm-yyyy")
        elif (d.isdigit() == False):
            messagebox.showinfo("Error", "Cost should be a number")
        else:
            insert(a, b, c, f)
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)

    def viewallitems():
        list1.delete(0, END)
        list1.insert(END, "{:<5} {:<12} {:<15} {:<8} {:<10}".format("ID", "NAME", "DATE", "COST", "CATEGORY"))

        for row in view():
            a, b, c, d, f = map(str, row)
            formatted_row = "{:<5} {:<12} {:<17} {:<14} {:<14}".format(a, b, c, d, f)
            list1.insert(END, formatted_row)

    def deletewithid():
        a = exp_id.get()
        delete(a)

    def searchItem():
        a = exp_itemname.get()
        b = exp_date.get()
        c = exp_cost.get()
        d = exp_categ.get()
        if (a == "" and b == "" and c == "" and d == ""):
            messagebox.showerror('Error', 'Field should not all be empty. Fill up only one field.')
        elif view() is None:
            messagebox.showinfo("No Data", "The database is empty. No items to search.")
        else:
            list1.delete(0, END)
            list1.insert(END, "ID    NAME       DATE        COST     CATEGORY")
            for row in search(exp_itemname.get(), exp_date.get(), exp_cost.get(), exp_categ.get()):
                a, b, c, d, e = map(str, row)
                formatted_row = f"{a:<6} {b:<12} {c:<12} {d:<10} {e:<10}"
                list1.insert(END, formatted_row)
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)

    def endPage():
        endphoto = PhotoImage(file="images/ThankYou.png")
        endlabel = Label(gui, border=0, bg='grey', image=endphoto)
        endlabel.photo = endphoto
        endlabel.place(x=0, y=0)
        Label(gui, font=("century", 25), bg="#DCFAF3", fg="black", text="This window closes in ").place(x=250, y=640)
        ltime = Label(gui, font=("century", 25), bg="#DCFAF3", fg="black")
        ltime.place(x=600, y=640)

        def timer():
            global t
            a = str(t) + " seconds"
            text_input = a
            ltime.config(text=text_input)
            ltime.after(1000, timer)
            t = t - 1

        timer()
        gui.after(11000, gui.destroy)

    # CASHWIZZ MAIN WINDOW
    gui = Tk()
    gui.title("CashWizz")
    gui.geometry("1000x700")
    gui.resizable(False, False)
    mainphoto = PhotoImage(file="images/MainWindow.png")
    mainlabel = Label(gui, border=0, bg='grey', image=mainphoto)
    mainlabel.pack(fill=BOTH)

    # Add item
    additem_image = PhotoImage(file="images/AddItem.png")
    additembtn = Button(gui, font=("helvetica", 20), command=insertitems, bg="#DCFAF3", image=additem_image,
                        borderwidth=0)
    additembtn.place(x=59, y=573)

    # Search item
    searchitem_image = PhotoImage(file="images/SearchItem.png")
    searchitembtn = Button(gui, font=("helvetica", 20), command=searchItem, bg="#DCFAF3", image=searchitem_image,
                           borderwidth=0)
    searchitembtn.place(x=278, y=573)

    # View item
    viewitem_image = PhotoImage(file="images/ViewExpenses.png")
    viewitembtn = Button(gui, font=("helvetica", 20), command=expensesTableGUI, bg="#8CEED7", image=viewitem_image,
                         borderwidth=0)
    viewitembtn.place(x=542, y=415)

    # Delete with id
    delid_image = PhotoImage(file="images/DelwithID.png")
    delidbtn = Button(gui, font=("helvetica", 20), command=deletewithid, bg="#8CEED7", image=delid_image, borderwidth=0)
    delidbtn.place(x=542, y=494)

    # Delete all items
    delall_image = PhotoImage(file="images/DelAll.png")
    delallbtn = Button(gui, font=("helvetica", 20), command=deletealldata, bg="#8CEED7", image=delall_image,
                       borderwidth=0)
    delallbtn.place(x=542, y=574)

    # Total spent
    total_image = PhotoImage(file="images/TotalSpent.png")
    totalbtn = Button(gui, font=("helvetica", 20), command=totalExpenses, bg="#8CEED7", image=total_image, borderwidth=0)
    totalbtn.place(x=756, y=415)

    # Close window
    ext_image = PhotoImage(file="images/ExitWindow.png")
    extbtn = Button(gui, font=("helvetica", 20), command=endPage, bg="#8CEED7", image=ext_image, borderwidth=0)
    extbtn.place(x=756, y=574)

    exp_id = StringVar()
    sb = Spinbox(gui, font=("helvetica", 16), from_=0, to_=200, textvariable=exp_id, justify=CENTER)
    sb.place(x=922, y=506, height=30, width=50)

    exp_itemname = StringVar()
    e1 = Entry(gui, font=("helvetica", 16), border=0, textvariable=exp_itemname, bg="#ffffff")
    e1.place(x=235, y=347, height=25, width=200)

    exp_date = StringVar()
    e2 = Entry(gui, font=("helvetica", 16), border=0, textvariable=exp_date, bg="#ffffff")
    e2.place(x=235, y=407, height=25, width=200)

    exp_cost = StringVar()
    e3 = Entry(gui, font=("helvetica", 16), border=0, textvariable=exp_cost, bg="#ffffff")
    e3.place(x=235, y=462, height=25, width=200)

    exp_categ = StringVar()
    e4 = Entry(gui, font=("helvetica", 16), border=0, textvariable=exp_categ, bg="#ffffff")
    e4.place(x=235, y=521, height=25, width=200)

    name = Label(gui, font=("century", 25, "bold"), text=profilename, bg="#DCFAF3", fg="#034744")
    name.place(relx=.85, rely=.2, anchor=CENTER)
    ltime = Label(gui, font=("century", 20), bg="#DCFAF3", fg="#034744")
    ltime.place(x=308, y=180)

    def digitalclock():
        if gui and gui.winfo_exists():  # Check if the window still exists
            text_input1 = time.strftime("%d-%m-%Y                %H:%M:%S")
            ltime.config(text=text_input1)
            gui.after(1000, digitalclock)

    digitalclock()
    gui.resizable(False, False)
    gui.mainloop()

def registerGUI():
    global register_name, register_username, register_password, register_confpass
    global reg_nameentry, reg_userentry, reg_passentry, reg_confpass

    # Register
    regui = Toplevel(root)
    regui.title("Register")
    regui.geometry("800x500")
    regui.wm_attributes('-transparentcolor', 'grey')
    regframe_label = Label(regui, border=0, bg='grey', image=regframe_photo)

    reg_namelabel = Label(regui, font=("arial black", 13), text="Name:", bg='#ffffff', fg='#034744').place(x=175, y=193)
    register_name = StringVar()
    reg_nameentry = Entry(regui, width=27, border=0, font=('helvetica', 14), textvariable=register_name, bg='#ffffff')
    reg_nameentry.place(x=250, y=193, height=30, width=340)
    regframe_label.pack(fill=BOTH)

    # Username na gagamitin sa account
    reg_userlabel = Label(regui, font=("arial black", 13), text="Username:", bg='#ffffff', fg='#034744').place(x=175,y=243)
    register_username = StringVar()
    reg_userentry = Entry(regui, width=27, border=0, font=('helvetica', 14), textvariable=register_username, bg='#ffffff')
    reg_userentry.place(x=290, y=243, height=30, width=340)

    # Password
    reg_passlabel = Label(regui, font=("arial black", 13), text="Password:", bg='#ffffff', fg='#034744').place(x=175,
                                                                                                              y=294)
    register_password = StringVar()
    reg_passentry = Entry(regui, width=27, border=0, font=('helvetica', 14), textvariable=register_password, bg='#ffffff',
                          show="*")
    reg_passentry.place(x=290, y=297, height=30, width=340)

    # Password checker kung same
    reg_confpasslabel = Label(regui, font=("arial black", 13), text="Confirm Password:", bg='#ffffff', fg='#034744').place(x=175, y=345)
    register_confpass = StringVar()
    reg_confpass = Entry(regui, width=20, border=0, font=('helvetica', 14), textvariable=register_confpass, bg='#ffffff',
                         show="*")
    reg_confpass.place(x=360, y=348, height=30, width=300)

    # reg button
    reg_image2 = Label(image=reg_btn)
    reg_button2 = Button(regui, font=("tahoma", 19), command=register, image=reg_btn, borderwidth=0, bg="#DCFAF3").place(
        x=223, y=407)

    regui.resizable(False,False)


# Main code
root = Tk()
root.configure(bg='#D1FFF4')
root.title("CashWizz")
root.geometry("1000x700")
root.wm_attributes('-transparentcolor', 'grey')
rframe_photo = PhotoImage(file="images/LoginPage.png")
rframe_label = Label(root, border=0, bg='grey', image=rframe_photo)
rframe_label.pack(fill=BOTH)

def digitalclock1():
    text_input1 = time.strftime("%d-%m-%Y")
    ldate.config(text=text_input1)

ldate = Label(root, font=("century", 20), bg="#034744", fg="white")
ldate.place(x=675, y=24)
digitalclock1()

# Login Button
login_btn = PhotoImage(file="images/login_btn.png")
login_image = Label(image=login_btn, text="Log in")
login_button = Button(root, text="Register", font=("helvetica", 19), command=login, image=login_btn, borderwidth=0,
                      bg="#8CEED7").place(x=551, y=356)

# Username
user_label = Label(root, font=("arial black", 13), text="Username:", bg='#DCFAF3', fg='#034744').place(x=620, y=233)
login_username = StringVar()
user_entry = Entry(root, width=27, border=0, font=('helvetica', 14), textvariable=login_username, bg='#DCFAF3', fg='#034744')
user_entry.place(x=730, y=235, width=200)

# Password
pass_label = Label(root, font=("arial black", 13), text="Password:", bg='#DCFAF3', fg='#034744').place(x=620, y=300)
login_password = StringVar()
pass_entry = Entry(root, width=27, border=0, font=('helvetica', 14), textvariable=login_password, show="*", bg='#DCFAF3', fg='#034744')
pass_entry.place(x=730, y=305, width=200)

# photo image import
regframe_photo = PhotoImage(file="images/Register.png")
reg_btn = PhotoImage(file="images/Sign up.png")
userTable_photo = PhotoImage(file="images/userTable.png")
endphoto = PhotoImage(file="images/ThankYou.png")

# reg button
reg_btn = PhotoImage(file="images/reg_btn.png")
reg_btn2 = PhotoImage(file="images/reg_btn.png")
reg_image = Label(image=reg_btn)
reg_button = Button(root, font=("tahoma", 19), command=registerGUI, image=reg_btn, borderwidth=0, bg="#8CEED7").place(x=551, y=468)

# View accounts button
va_btn = PhotoImage(file="images/viewAcc.png")
va_image = Label(image=va_btn)
va_button = Button(root, font=("tahoma", 19), command=viewwindow, image=va_btn, borderwidth=0, bg="#8CEED7").place(
    x=551, y=557)

# Delete users button
del_btn = PhotoImage(file="images/delUsers.png")
del_image = Label(image=del_btn)
del_button = Button(root, font=("tahoma", 19), command=deleteAllUsers, image=del_btn, borderwidth=0,
                    bg="#8CEED7").place(x=756, y=557)

root.resizable(False, False)
root.mainloop()
