import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk
from PIL import Image
# from serial import time



from DBConnection import Db
i=0
images = []


static_path=r"D:\Project softwares\Project\Secure_ATM\Secure_ATM_app\static\\"

def otppage1(result):

    root = Tk()
    root.geometry('780x550+20+0')
    root.title("RAVENBANK")

    canvas = Canvas(width=200, height=200)
    canvas.pack(expand=YES, fill=BOTH)

    image = ImageTk.PhotoImage(file=static_path + "fp.jpg")
    images.append(image)
    canvas.create_image(0, 0, image=image, anchor=NW)

    canvas = Canvas(root, width=100, height=150)
    canvas.place(relx=0.1, rely=0.5)
    ######################################
    ######################################
    db=Db()

    ######################################
    ######################################
     # img = img.zoom(25)  # with 250, I ended up running out of memory
    # img = img.subsample(32)  # mechanically, here it is adjusted to 32 instead of 320


    # images.append(img)
    # canvas.create_image(0, 0, anchor=NW, image=img)





    l2 = Label(root, text="ATM", font="Helvetica 25 bold")
    l2.place(relx=0.5, rely=0.05)

    l3 = Label(root, text="RAVENBANK", font="Helvetica 45 bold")
    l3.place(relx=0.3, rely=0.25)


    def btnclick():
        amt=e1.get()
        if float(result['amount'])>float(amt):
            db=Db()
            db.update("update secure_atm_app_customer set amount=amount-'"+str(amt)+"' where id='"+str(result['user_id'])+"'")
            db.insert("insert into secure_atm_app_transactions values(null, curdate(), curtime(), '"+str(amt)+"', 'Withdraw', '"+str(result['user_id'])+"')")
            messagebox.showinfo("Authentication", "Successfull")
            root.destroy()
            from tu import homefn
        else:
            messagebox.showinfo("Authentication", "Insufficient Balance")
            root.destroy()
            from tu import homefn



    l2 = Label(root, text="Please enter your Amount",font="Helvetica 15 bold")
    l2.place(relx=0.25, rely=0.55)

    e1=Entry(root, justify = CENTER,
                                     font = ('courier', 15, 'bold'))
    e1.place(relx=0.6,rely=0.55)

    b1 =Button(root, text="Withdraw", command=btnclick,font =('Helvetica', 10, 'bold', 'underline'), foreground = 'black',borderwidth = '4')
    b1.place(relx=0.475, rely=0.7 )

    root.mainloop()
# otppage1((8,'naveen',100.0),13)