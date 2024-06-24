import tkinter
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

from PIL import ImageTk

import random
import string

from DBConnection import Db

static_path=r"D:\Project softwares\Project\Secure_ATM\Secure_ATM_app\static\\"

def homefn():

    root=Tk()
    root.geometry('780x550+20+0')
    root.wm_iconbitmap(static_path + 'sync.ico')
    root.title("RAVENBANK")

    canvas = Canvas(width=200, height=200)
    canvas.pack(expand=YES, fill=BOTH)

    image = ImageTk.PhotoImage(file=static_path + "hp.jpg")
    canvas.create_image(0, 0, image=image, anchor=NW)




    def btnclick():
        card=e1.get()
        print(card)
        db = Db()
        result = db.selectOne(
            "select secure_atm_app_customer.name, secure_atm_app_customer.email, secure_atm_app_customer.id as user_id, secure_atm_app_customer.amount, secure_atm_app_atm_card.id as atm_id, secure_atm_app_atm_card.status from secure_atm_app_atm_card join secure_atm_app_customer on secure_atm_app_atm_card.USER_id=secure_atm_app_customer.id where secure_atm_app_atm_card.card_no='" + str(
                card) + "'")
        # result=cmd.fetchone()
        if result is not None:
            stat = result['status']
            if stat == "blocked":
                messagebox.showinfo("Authentication", "Card is in blocked state")
                root.destroy()
                from first_page import homefn
            else:
                messagebox.showinfo("Authentication", "Please face the camera")
                root.destroy()

                #################
                from camera import abc
                obj = abc()
                resss = obj.check_face(str(result['user_id']), str(result['atm_id']))
                if resss == "ok":
                    messagebox.showinfo("Authentication", "Face recognized")
                    password_characters = string.ascii_letters + string.digits
                    pwd = ''.join(random.choice(password_characters) for i in range(5))
                    print("OTPPPPPPP    ", pwd)
                    import smtplib
                    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
                    s.starttls()
                    s.login("secureatm408@gmail.com", "gwfoznfdurxqubyh")  # change mail
                    msg = MIMEMultipart()  # create a message.........."
                    msg['From'] = "secureatm408@gmail.com"
                    msg['To'] = result['email']
                    msg['Subject'] = "Your OTP for Secure ATM Website"
                    body = "Please transfer the otp to the authorised person if transaction not initiated by card owner..\nOTP  :  " + str(pwd)
                    msg.attach(MIMEText(body, 'plain'))
                    s.send_message(msg)

                    # redirect to otp page
                    from otp import otppage
                    cnt = 0
                    otppage(result, pwd, cnt)


                else:
                    messagebox.showinfo("Authentication", "Fraud user detected")

        else:
            messagebox.showinfo("Authentication", "Swipe card again")

    l2= Label(root,text="ATM",font = "Helvetica 25 bold")
    l2.place(relx=0.5,rely=0.05)

    l3 = Label(root, text="RAVENBANK", font="Helvetica 45 bold")
    l3.place(relx=0.3, rely=0.25)

    l4 = Label(root, text="Please enter card number", font="Helvetica 20 bold")
    l4.place(relx=0.15, rely=0.45)

    e1 = Entry(root)
    e1.place(relx=0.30, rely=0.55)

    b1 = Button(root, text="Next", command=btnclick)
    b1.place(relx=0.475, rely=0.8)




    root.mainloop()
homefn()