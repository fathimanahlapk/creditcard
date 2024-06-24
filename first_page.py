import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

from PIL import ImageTk
static_path=r"D:\Project softwares\Project\Secure_ATM\Secure_ATM_app\static\\"

def homefn():

    root=Tk()
    root.geometry('780x550+20+0')                   #           window size
    root.wm_iconbitmap(static_path + 'sync.ico')
    root.title("RAVENBANK")

    canvas = Canvas(width=200, height=200)
    canvas.pack(expand=YES, fill=BOTH)

    image = ImageTk.PhotoImage(file=static_path + "fp.jpg")
    canvas.create_image(0, 0, image=image, anchor=NW)               #   load background





    def nextpage():
        root.destroy()                  #           close current window
        from home import homefn

    b1=Button(root,text="START",command=nextpage)
    b1.place(relx=0.58,rely=0.85)

    l2= Label(root,text="ATM",font = "Helvetica 25 bold")
    l2.place(relx=0.5,rely=0.05)

    l3 = Label(root, text="RAVENBANK", font="Helvetica 45 bold")
    l3.place(relx=0.3, rely=0.25)

    l4 = Label(root, text="WELCOME TO OUR ATM", font="Helvetica 35 bold")
    l4.place(relx=0.2, rely=0.45)


    root.mainloop()
homefn()