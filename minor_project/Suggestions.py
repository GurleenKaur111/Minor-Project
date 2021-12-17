from tkinter import *
from PIL import Image,ImageTk
import webbrowser

def suggestions(r):
    
    window=Toplevel(r)	
    window.title("Suggestions")
    window.geometry("1350x700+0+0")

    bg = PhotoImage(file = "light_bgd.png")
    label1 = Label( window, image = bg)
    label1.place(x = 0, y = 0)


    frame1=Frame(window,highlightbackground = "#053742", highlightcolor= "#053742",highlightthickness=2,bg="#f7f7f7")
    frame1.place(x=250,y=160,width=800,height=300)

    Label(frame1,text="For further queries and suggestions, Please Contact:",font=("times new roman",25,"bold"),fg="#053742",bg="#f7f7f7").place(x=35,y=30)   

    Label(frame1,text="Aastha Agarwal",font=("times new roman",20,"bold"),fg="#36d7ff",bg="#f7f7f7").place(x=60,y=90)	
    Label(frame1,text="Arsh Bhatia",font=("times new roman",20,"bold"),fg="#36d7ff",bg="#f7f7f7").place(x=60,y=135)
    Label(frame1,text="Ginnie Kaur",font=("times new roman",20,"bold"),fg="#36d7ff",bg="#f7f7f7").place(x=60,y=180)
    Label(frame1,text="Gurleen Kaur",font=("times new roman",20,"bold"),fg="#36d7ff",bg="#f7f7f7").place(x=60,y=220)

    Label(frame1,text="aasthaagarwal91148@gmail.com",font=("times new roman",20,"bold"),fg="#053742",bg="#f7f7f7").place(x=350,y=90,height=35)  
    Label(frame1,text="arshbhatia2311@gmail.com",font=("times new roman",20,"bold"),fg="#053742",bg="#f7f7f7").place(x=350,y=135,height=35)
    Label(frame1,text="ginnykaur55002@gmail.com",font=("times new roman",20,"bold"),fg="#053742",bg="#f7f7f7").place(x=350,y=180,height=35)
    Label(frame1,text="gurleenkaur2520@gmail.com",font=("times new roman",20,"bold"),fg="#053742",bg="#f7f7f7").place(x=350,y=220,height=35)


    window.mainloop()