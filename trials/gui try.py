from tkinter import *
from tkinter import messagebox
import sqlite3
#from PIL import ImageTk, Image

def resize_image(event):
    new_width = 10
    new_height = 10

    image = copy_of_image.resize((new_width, new_height))
    photo = PhotoImage(image)

    label.config(image=photo)
    label.image = photo

def endpage():

    e = Tk()
    e.geometry('1000x700')
    e.title("CashWizz")
    e.wm_attributes('-transparentcolor', 'grey')
    frame_photo = PhotoImage(file="Frame 1.png")
    frame_label = Label(e, border=0, bg='grey', image=frame_photo)

    frame_label.pack(fill=BOTH)

    #frame_logolabel.bind('<Configure>', resize_image)
    e.resizable(False, False)
    e.mainloop()

endpage()

'''

root = Tk()
root.configure(bg='#0066ff')
frame = Frame(bd=0, highlightthickness=0, background="#751aff").place(relx=0.46, y=0, relwidth=1, relheight=1)
frame2 = Frame(bd=0, highlightthickness=0, background="#33cccc").place(x=0, rely=0.78, relwidth=1, relheight=1)
root.title("LOGIN / REGISTER")
root.geometry("1000x700")
l1 = Label(root, font=("comic sans ms", 19), bg="#0066ff", text="Username").place(x=80, y=230)
l2 = Label(root, font=("comic sans ms", 19), bg="#0066ff", text="Password").place(x=80, y=280)
b1 = Button(root, text="Login", font=("algerian", 19), activebackground="#fffa66", activeforeground="red", width=12,
            command=login).place(x=110, y=360)
l6 = Label(root, font=("comic sans ms", 19), bg="#751aff", text="Name").place(x=653, y=195)
l3 = Label(root, font=("comic sans ms", 19), bg="#751aff", text="Username").place(x=604, y=243)
l4 = Label(root, font=("comic sans ms", 19), bg="#751aff", text="Password").place(x=610, y=293)
l5 = Label(root, font=("comic sans ms", 17), bg="#751aff", text="Confirm password").place(x=532, y=342)
b2 = Button(root, text="Register", font=("algerian", 19), activebackground="#fffa66", activeforeground="red", width=12,
            command=register).place(x=630, y=400)

root.resizable(False, False)
root.mainloop()

'''