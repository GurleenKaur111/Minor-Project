from tkinter import *
import mysql.connector
import signup
from PIL import ImageTk,Image 
import webbrowser
import Curls
import DumbellPress
import LateralRaise
import Squats
import TricepsExtension

def callback(url): 
	webbrowser.open_new_tab(url)

def menu(r,i,n):
	window=Toplevel(r)
	window.title("Menu")
	window.geometry("1350x700+0+0")

	heading1=Label(window,text=n,font=("times new roman",20,"bold"),fg="#053742",bg="#E8F0F2",width="500",height="2")
	heading1.place(x=300,y=0,width=700,height=70)

	heading2=Label(window,text=i,font=("times new roman",20,"bold"),fg="#053742",bg="#E8F0F2",width="500",height="2")
	heading2.place(x=1000,y=0,width=280,height=70)

	top_left = Frame(window,highlightbackground = "#053742", highlightcolor= "#053742",highlightthickness=2,bg="#A2DBFA")
	top_left.place(x=0,y=0,width=298,height=258)
	c1 = ImageTk.PhotoImage(Image.open('Logo.png'))
	c1_label = Label(top_left, image=c1)
	c1_label.pack()

	frame1=Frame(window,highlightbackground = "#053742", highlightcolor= "#053742",highlightthickness=2,bg="#A2DBFA")
	frame1.place(x=0,y=260,width=298,height=388)

	frame2=Frame(window,highlightbackground = "#053742", highlightcolor= "#053742",highlightthickness=2,bg="#A2DBFA")
	frame2.place(x=300,y=70,width=700,height=578)

	Button(frame1,text="PROFILE",font=("times new roman",16,"bold"),fg="#053742",bg="#E8F0F2").place(x=30,y=80,width=220,height=40)
	Button(frame1,text="PERFORMANCE",font=("times new roman",16,"bold"),fg="#053742",bg="#E8F0F2").place(x=30,y=160,width=240,height=40)
	Button(frame1,text="HELP",font=("times new roman",16,"bold"),fg="#E8F0F2",bg="red").place(x=30,y=300,width=220,height=35)

	frame3=Frame(window,highlightbackground = "#053742", highlightcolor= "#053742",highlightthickness=2,bg="#A2DBFA")
	frame3.place(x=1002,y=70,width=267,height=578)

	Label(frame2,text="Recommendation",font=("times new roman",25,"bold"),fg="#053742",bg="#A2DBFA").place(x=230,y=35)

	Label(frame2,text="1. Why nutrition is the most important part of Fitness?",font=("times new roman",16,"bold"),fg="#053742",bg="#A2DBFA").place(x=20,y=120)
	Button(frame2,text="Read More",font=("times new roman",12,"bold"),fg="#053742",bg="#E8F0F2", command=lambda:callback("https://www.verywellfit.com/eat-healthy-feel-healthy-and-look-amazing-3121363")).place(x=44,y=155,width=100,height=20)
	Label(frame2,text="2. Ten Super foods to eat daily for optimal health.",font=("times new roman",16,"bold"),fg="#053742",bg="#A2DBFA").place(x=20,y=190)
	Button(frame2,text="Read More",font=("times new roman",12,"bold"),fg="#053742",bg="#E8F0F2", command=lambda:callback("https://www.verywellfit.com/eat-a-wide-variety-of-superfoods-3121399")).place(x=44,y=225,width=100,height=20)
	Label(frame2,text="3. The Best protein bars for Women, according to dietitian.",font=("times new roman",16,"bold"),fg="#053742",bg="#A2DBFA").place(x=20,y=265)
	Button(frame2,text="Read More",font=("times new roman",12,"bold"),fg="#053742",bg="#E8F0F2", command=lambda:callback("https://www.verywellfit.com/best-protein-bars-for-women-4172473")).place(x=44,y=300,width=100,height=20)
	Label(frame2,text="4. The Connection between Diet, Exercise, and Sleep.",font=("times new roman",16,"bold"),fg="#053742",bg="#A2DBFA").place(x=20,y=335)
	Button(frame2,text="Read More",font=("times new roman",12,"bold"),fg="#053742",bg="#E8F0F2", command=lambda:callback("https://www.sleepfoundation.org/physical-health/diet-exercise-sleep")).place(x=44,y=370,width=100,height=20)
	Label(frame2,text="5. Top Fitness Trends of 2021- Best Workout tips and Health trends.",font=("times new roman",16,"bold"),fg="#053742",bg="#A2DBFA").place(x=20,y=405)
	Button(frame2,text="Read More",font=("times new roman",12,"bold"),fg="#053742",bg="#E8F0F2", command=lambda:callback("https://www.elle.com/uk/life-and-culture/culture/longform/a41063/fitness-trends-gym-classes-workout/")).place(x=44,y=440,width=100,height=20)

	Label(frame3,text="1. Curls",font=("times new roman",18,"bold"),fg="#053742",bg="#A2DBFA").place(x=30,y=35)
	Button(frame3,text="Tutorial",font=("times new roman",14,"bold"),fg="#053742",bg="#E8F0F2", command=lambda:callback("https://www.youtube.com/watch?v=av7-8igSXTs&list=PL6cJnPFy3bBn5Aiup3qm68q35FI12nVd_&index=1")).place(x=30,y=75,width=110,height=20)
	Button(frame3,text="Start",font=("times new roman",14,"bold"),fg="#053742",bg="#E8F0F2",command=lambda:Curls.Curls()).place(x=145,y=75,width=110,height=20)

	Label(frame3,text="2. Dumbbell Press",font=("times new roman",18,"bold"),fg="#053742",bg="#A2DBFA").place(x=30,y=135)
	Button(frame3,text="Tutorial",font=("times new roman",14,"bold"),fg="#053742",bg="#E8F0F2", command=lambda:callback("https://www.youtube.com/watch?v=B-aVuyhvLHU&list=PL6cJnPFy3bBn5Aiup3qm68q35FI12nVd_&index=2")).place(x=30,y=175,width=110,height=20)
	Button(frame3,text="Start",font=("times new roman",14,"bold"),fg="#053742",bg="#E8F0F2",command=lambda:DumbellPress.DumbellPress()).place(x=145,y=175,width=110,height=20)

	Label(frame3,text="3. Lateral Raise",font=("times new roman",18,"bold"),fg="#053742",bg="#A2DBFA").place(x=30,y=235)
	Button(frame3,text="Tutorial",font=("times new roman",14,"bold"),fg="#053742",bg="#E8F0F2", command=lambda:callback("https://www.youtube.com/watch?v=kDqklk1ZESo&list=PL6cJnPFy3bBn5Aiup3qm68q35FI12nVd_&index=3")).place(x=30,y=275,width=110,height=20)
	Button(frame3,text="Start",font=("times new roman",14,"bold"),fg="#053742",bg="#E8F0F2",command=lambda:LateralRaise.LateralRaise()).place(x=145,y=275,width=110,height=20)

	Label(frame3,text="4. Squats",font=("times new roman",18,"bold"),fg="#053742",bg="#A2DBFA").place(x=30,y=335)
	Button(frame3,text="Tutorial",font=("times new roman",14,"bold"),fg="#053742",bg="#E8F0F2", command=lambda:callback("https://www.youtube.com/watch?v=6AEDbzzFGsM&list=PL6cJnPFy3bBn5Aiup3qm68q35FI12nVd_&index=4")).place(x=30,y=375,width=110,height=20)
	Button(frame3,text="Start",font=("times new roman",14,"bold"),fg="#053742",bg="#E8F0F2",command=lambda:Squats.Squats()).place(x=145,y=375,width=110,height=20)

	Label(frame3,text="5. Triceps Extension",font=("times new roman",18,"bold"),fg="#053742",bg="#A2DBFA").place(x=30,y=445)
	Button(frame3,text="Tutorial",font=("times new roman",14,"bold"),fg="#053742",bg="#E8F0F2", command=lambda:callback("https://www.youtube.com/watch?v=nRiJVZDpdL0&list=PL6cJnPFy3bBn5Aiup3qm68q35FI12nVd_&index=5")).place(x=30,y=485,width=110,height=20)
	Button(frame3,text="Start",font=("times new roman",14,"bold"),fg="#053742",bg="#E8F0F2",command=lambda:TricepsExtension.TricepsExtension()).place(x=145,y=485,width=110,height=20)

	window.mainloop()