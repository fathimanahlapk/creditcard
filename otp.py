import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk

# from bank.newpae import homepage

i=0

static_path=r"D:\Project softwares\Project\Secure_ATM\Secure_ATM_app\static\\"

from DBConnection import Db
def otppage(result,otp, cnt):
    root = Tk()
    root.geometry('780x550+20+0')
    root.wm_iconbitmap(static_path + 'sync.ico')
    root.title("RAVENBANK")

    canvas = Canvas(width=200, height=200)
    canvas.pack(expand=YES, fill=BOTH)

    image = ImageTk.PhotoImage(file=static_path + "fp.jpg")
    canvas.create_image(0, 0, image=image, anchor=NW)



        # root.after(1, Recive)

    def btnclick():
        cotp=e1.get()
        cnt=l4.cget("text")
        print("Cnt ", cnt)

        if otp==cotp:
            messagebox.showinfo("Authentication", "Success")
            # root.destroy()
            from final import otppage1
            otppage1(result)
        else:

            cnt=int(cnt)-1
            print("NNN  ", cnt)
            l4.config(text = str(cnt))
            if cnt == 0:
                import cv2
                webcam=cv2.VideoCapture(0)
                check, frame=webcam.read()
                import time
                dt=time.strftime("%Y%m%d_%H%M%S")
                cv2.imwrite(static_path + "block_images\\" + dt + ".jpg", frame)
                path="/static/block_images/" + dt + ".jpg"

                db=Db()
                db.insert("insert into secure_atm_app_block_details values(null, curdate(),curtime(), 'blocked', '"+path+"', '"+str(result['atm_id'])+"')")
                db.update("update secure_atm_app_atm_card set status='blocked' where id='"+str(result['atm_id'])+"'")
                messagebox.showinfo("Authentication", "Account Blocked")
                root.destroy()
                from first_page import homefn



    print("cnt  ", cnt)
    # l2 = Label(root, text="ATM", font="Helvetica 25 bold")
    # l2.place(relx=0.5, rely=0.05)

    l4 = Label(root, text="3", font="Helvetica 25 bold")
    l4.place(relx=0.9, rely=0.09)
    l5 = Label(root, text="Chances left", font="Helvetica 25 bold")
    l5.place(relx=0.6, rely=0.09)

    l3 = Label(root, text="RAVENBANK", font="Helvetica 45 bold")
    l3.place(relx=0.3, rely=0.25)

    l2 = Label(root, text="Hi "+result['name']+"! Please enter your OTP",font="Helvetica 20 bold")
    l2.place(relx=0.15, rely=0.45)

    e1=Entry(root)
    e1.place(relx=0.30,rely=0.55)

    b1 =Button(root, text="Next", command=btnclick)
    b1.place(relx=0.475, rely=0.8)
    # root.after(1, Recive)
    root.mainloop()
# otppage((8,'naveen',100.0),"12345",13)