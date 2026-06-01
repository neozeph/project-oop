from tkinter import *


def endpage():
    Label(gui, width=100, height=100, font=("century", 35), bg="#bfbfbf", text="").place(x=-455, y=0)
    Label(gui, font=("lucida fax", 40), bg="#bfbfbf", text="EXPENSE TRACKER").place(x=190, y=10)
    Label(gui, font=("gabriola", 40), bg="#bfbfbf", text="An application developed using").place(x=70, y=170)
    Label(gui, font=("gabriola", 40), bg="#bfbfbf", text="sqlite3 and tkinter").place(x=400, y=250)
    Label(gui, font=("ink free", 35), bg="#bfbfbf", text="R Harsha").place(x=500, y=450)
    #h = Label(gui, font=("century", 25), bg="#bfbfbf", text="This window auomatically closes after")
    #h.place(x=65, y=650)
    #ltime = Label(gui, font=("century", 25), bg="#bfbfbf", fg="black")
    #ltime.place(x=655, y=651)

    def timer():
        global t
        a = str(t) + " seconds"
        text_input = a
        ltime.config(text=text_input)
        ltime.after(1000, timer)
        t = t - 1

    timer()
    gui.after(11000, gui.destroy)

endpage()

'''
frame = Frame(win, width=627, height=459)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("Project.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

win.mainloop()
'''
'''

from tkinter import *

root = Tk()
root.geometry('627x459')
root.overrideredirect(1)
root.wm_attributes("-transparentcolor", "grey")


def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')


frame_photo = PhotoImage(file='Project.png')
frame_label = Label(root, border=0, bg='grey', image=frame_photo)
frame_label.pack(fill=BOTH, expand=True)

frame_label.bind("<B1-Motion>", move_app)

root.mainloop()

'''