from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import os

class  Login:
    def __init__(self,login):
        self.login = l
        l.title("Login")
        l.geometry("330x360+550+150")
        l.configure(bg='whitesmoke')

        img1 = Image.open(r"C:\Users\KalKun\Desktop\Sem-4 Mini Project\Images\2.jpg")
        img1 = img1.resize((100,100),Image.ANTIALIAS)
        self.p1 = ImageTk.PhotoImage(img1)
        
        L1 = Label(l,image=self.p1)
        L1.place(x=100,y=10,width=100,height=100)

        L2 = Label(l,text = "Username",font = ("times new roman",12,"bold"),bg='whitesmoke',fg="black")
        L2.place(x=30,y=150,width=70,height=20)

        self.T1 = Entry(l,font = ("times new roman",12,"bold"),bd=2,bg="gray80",fg="blue")
        self.T1.place(x=30,y=180,width=270,height=20)

        L3 = Label(l,text = "Password",font = ("times new roman",12,"bold"),bg='whitesmoke',fg="black")
        L3.place(x=30,y=200,width=65,height=20)

        self.T2 = Entry(l,show="*",font = ("times new roman",15,"bold"),bd=2,bg="gray80",fg="firebrick3")
        self.T2.place(x=30,y=230,width=270,height=20)

        b1 = Button(l,command=self.lb,text="Login",font = ("times new roman",16,"bold"),bd=3,relief="raised",bg="royal blue3",fg="white",activebackground="royal blue3",activeforeground="black")
        b1.place(x=100,y=270,width=120,height=30)
    
        b2 = Button(l,command=self.cb,text="Sign Up",font = ("times new roman",12,"bold"),borderwidth=0,bg="whitesmoke",fg="black",activeforeground="blue")
        b2.place(x=100,y=320,width=120,height=17)
        
    def cb(self):
        f='manager.py'
        os.system(f)

    def lb(self):
        if (self.T1.get()=="Kalpesh" and self.T2.get()=="1234") or (self.T1.get()=="Manish" and self.T2.get()=="manish"):
            messagebox.showinfo("Success","Login Successful")
            f='dashboard.py'
            os.system(f)
        else:
            messagebox.showerror("Error","Please enter valid username and password")

if __name__ == "__main__":
    l=Tk()
    object=Login(l)
    l.mainloop()