from tkinter import *
import mysql.connector
from mysql.connector import errorcode
import tkinter.messagebox
from PIL import Image,ImageTk
import Developers

def signup(r):

	window=Toplevel(r)	
	window.title("Sign Up")
	window.geometry("1350x700+0+0")

	bg = PhotoImage(file = "light_bgd.png")
	label1 = Label(window, image = bg)
	label1.place(x = 0, y = 0)

	top_left = Frame(window,highlightbackground = "#053742", highlightcolor= "#053742",highlightthickness=2,bg="#A2DBFA")
	top_left.place(x=227,y=100,width=250,height=500)
	c1 = ImageTk.PhotoImage(Image.open('exer2.png'))
	
	c1_label = Label(top_left, image=c1)
	c1_label.pack()

	
	frame1=Frame(window,highlightbackground = "#053742", highlightcolor= "#053742",highlightthickness=2,bg="#A2DBFA",)
	frame1.place(x=480,y=100,width=500,height=500)

	heading=Label(frame1,text="SIGN UP",font=("times new roman",20,"bold"),fg="#053742",bg="#E8F0F2",width="500",height="2").pack()

	userid=IntVar()
	username=StringVar()
	useremail=StringVar()
	passcode=StringVar()
	confirm=StringVar()

	def insert():
		ui=int(userid.get())
		un=str(username.get())
		umail=str(useremail.get())
		p=str(passcode.get())
		db=mysql.connector.connect(host="localhost" ,user="root", password="1234", database="exercise")
		cursor=db.cursor()

		if ui=="" or p=="" or un=="" or umail=="":
			tkinter.messagebox.showinfo('Error', "Enter all the details!!!!")


		try:	
			cursor.execute("insert into users values(%d,'%s','%s','%s')"%(ui,un,umail,p))
			tkinter.messagebox.showinfo('Success', "Registration Successful!!!")

		except mysql.connector.Error as err:
			if err.errno == 1062:
				tkinter.messagebox.showinfo('Error', "User Id already used, try again!!!")
				
		db.commit()
		db.close()

	Label(frame1,text="User Id",font=("times new roman",12,"bold"),fg="#053742",bg="#A2DBFA").place(x=50,y=100)	
	Label(frame1,text="User Name",font=("times new roman",12,"bold"),fg="#053742",bg="#A2DBFA").place(x=50,y=145)
	Label(frame1,text="Email Id",font=("times new roman",12,"bold"),fg="#053742",bg="#A2DBFA").place(x=50,y=190)
	Label(frame1,text="Password",font=("times new roman",12,"bold"),fg="#053742",bg="#A2DBFA").place(x=50,y=235)
	Label(frame1,text="Confirm Password",font=("times new roman",12,"bold"),fg="#053742",bg="#A2DBFA").place(x=50,y=280)

	Entry(frame1,textvariable=userid,font=("times new roman",15),bg="#E8F0F2").place(x=200,y=100,width=230)
	Entry(frame1,textvariable=username,font=("times new roman",15),bg="#E8F0F2").place(x=200,y=145,width=230)
	Entry(frame1,textvariable=useremail,font=("times new roman",15),bg="#E8F0F2").place(x=200,y=190,width=230)
	Entry(frame1,textvariable=passcode,show="*",font=("times new roman",15),bg="#E8F0F2").place(x=200,y=235,width=230)
	Entry(frame1,textvariable=confirm,show="*",font=("times new roman",15),bg="#E8F0F2").place(x=200,y=280,width=230)
	
	Button(frame1,text="SIGN UP",command=insert,font=("times new roman",12),fg="#053742",bg="#E8F0F2").place(x=170,y=340)

	Button(frame1,text="DEVELOPERS",command=lambda:Developers.developers(window),font=("times new roman",12),fg="#053742",bg="#E8F0F2").place(x=160,y=400)

	window.mainloop()

