from tkinter import *
from PIL import Image,ImageTk
import webbrowser

def developers(r):
    def callback1():
            webbrowser.open_new(r"https://www.linkedin.com/in/aastha-agarwal-2579b3191/")

    def callback2():
            webbrowser.open_new(r"https://www.linkedin.com/in/arshbhatia23/")

    def callback3():
            webbrowser.open_new(r"https://www.linkedin.com/in/ginniekaur/")

    def callback4():
            webbrowser.open_new(r"https://www.linkedin.com/in/gurleen-kaur-36ab52201/")       


    window=Toplevel(r)	
    window.title("Developers")
    window.geometry("1350x700+0+0")

    bg = PhotoImage(file = "light_bgd.png")
  
    label1 = Label( window, image = bg)
    label1.place(x = 0, y = 0)

    frame1=Frame(window,highlightbackground = "#053742", highlightcolor= "#053742",highlightthickness=2,bg="#A2DBFA")
    frame1.place(x=330,y=160,width=600,height=250)

    Label(window,text="Aastha Agarwal 00113202718",font=("times new roman",20,"bold"),fg="#053742",bg="#A2DBFA").place(x=400,y=200)	
    Label(window,text="Arsh Bhatia 01313202718",font=("times new roman",20,"bold"),fg="#053742",bg="#A2DBFA").place(x=400,y=245)
    Label(window,text="Ginnie Kaur 02513202718",font=("times new roman",20,"bold"),fg="#053742",bg="#A2DBFA").place(x=400,y=290)
    Label(window,text="Gurleen Kaur 02813202718",font=("times new roman",20,"bold"),fg="#053742",bg="#A2DBFA").place(x=400,y=335)

    Button(window,text="in",font=("times new roman",20,"bold"),fg="#ffffff",bg="#0e76a8",command=callback1).place(x=800,y=200,height=35)  
    Button(window,text="in",font=("times new roman",20,"bold"),fg="#ffffff",bg="#0e76a8",command=callback2).place(x=800,y=245,height=35)
    Button(window,text="in",font=("times new roman",20,"bold"),fg="#ffffff",bg="#0e76a8",command=callback3).place(x=800,y=290,height=35)
    Button(window,text="in",font=("times new roman",20,"bold"),fg="#ffffff",bg="#0e76a8",command=callback4).place(x=800,y=335,height=35)

    window.mainloop()