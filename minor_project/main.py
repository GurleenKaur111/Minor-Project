from tkinter import *
import mysql.connector
import signup
from PIL import ImageTk,Image 
import tkinter.messagebox
import menu
import Developers

window=Tk()
window.title("Sign In")
window.geometry("1350x700+0+0")

bg = PhotoImage(file = "bgd.png")
  
label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)

frame1=Frame(window,highlightbackground = "#053742", highlightcolor= "#053742",highlightthickness=2,bg="#A2DBFA")
frame1.place(x=480,y=100,width=500,height=400)

heading=Label(frame1,text="SIGN IN",font=("times new roman",20,"bold"),fg="#053742",bg="#E8F0F2",width="500",height="2").pack()

userid=IntVar()
passcode=StringVar()

top_left = Frame(window,highlightbackground = "#053742", highlightcolor= "#053742",highlightthickness=2,bg="#A2DBFA")
top_left.place(x=227,y=100,width=250,height=400)
c1 = ImageTk.PhotoImage(Image.open('exer1.png'))
c1_label = Label(top_left, image=c1)
c1_label.pack()

def check():
		u=int(userid.get())
		p=str(passcode.get())

		if u<=0 or len(p) == 0:
			tkinter.messagebox.showinfo('Error', "Enter User Name And Password!!!!")

		else:
			db=mysql.connector.connect(host="localhost" ,user="root", password="1234", database="exercise")
			cursor=db.cursor()
			cursor.execute("select * from users where uid=%d and password='%s'"%(u,p))
			row=cursor.fetchone()

			if row==None:
				tkinter.messagebox.showinfo('Error', "Invalid Credentials/Account doesn't exists!!!")

			else:
				(uid, uname, uemail, password) = row
				print(row)
				print(uid)
				print(uname)
				menu.menu(window,uid,uname)

			db.commit()
			db.close()

Label(frame1,text="User Id",font=("times new roman",12,"bold"),fg="#053742",bg="#A2DBFA").place(x=50,y=100)
Label(frame1,text="Password",font=("times new roman",12,"bold"),fg="#053742",bg="#A2DBFA").place(x=50,y=145)

Entry(frame1,textvariable=userid,font=("times new roman",15),bg="#E8F0F2").place(x=200,y=100,width=230)
Entry(frame1,textvariable=passcode,show="*",font=("times new roman",15),bg="#E8F0F2").place(x=200,y=145,width=230)

Button(frame1,text="SIGN IN",command=check,font=("times new roman",12),fg="#053742",bg="#E8F0F2").place(x=170,y=200)
Button(frame1,text="New User? Register",command=lambda:signup.signup(frame1),font=("times new roman",12),fg="#053742",bg="#E8F0F2").place(x=140,y=240)
Button(frame1,text="DEVELOPERS",width="25",command=lambda:Developers.developers(window),font=("times new roman",12),fg="#053742",bg="#E8F0F2").place(x=100,y=350)

window.mainloop()