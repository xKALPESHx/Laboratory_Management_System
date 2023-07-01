from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import Tk
import mysql.connector
import os

#=======================================
root= Tk()
root.title("DATA ENTRY")
root.geometry("1550x800+-10+0")
root.config(bg="light steel blue")
titel=Label(text="Data Entry",font=("Times New Roman",30,"bold"),bg="light steel blue",fg="black").place(x=550,y=10,width=500)

def c():
        f='Ragister.py'
        os.system(f)
def b():
        f='stock.py'
        os.system(f)
def d():
        f='chemical.py'
        os.system(f)
def a():
        f='b1.py'
        os.system(f)
def q():
        f='b2.py'
        os.system(f)
def p():
        f='assproject.py'
        os.system(f)

b1 = Button(root,command=c,text="Employee Registration",font = ("Times New Roman",15,"bold"),bg="wheat4",fg="black",activebackground="wheat4").place(x=50,y=120,width=250,height=50)
b2 = Button(root,command=b,text="Purchased Apparatus",font = ("Times New Roman",15,"bold"),bg="wheat4",fg="black",activebackground="wheat4").place(x=50,y=210,width=250,height=50)
b3 = Button(root,command=d,text="Purchased Chemical",font = ("Times New Roman",15,"bold"),bg="wheat4",fg="black",activebackground="wheat4").place(x=50,y=300,width=250,height=50)
b4 = Button(root,command=a,text="Borrow Apparatus",font = ("Times New Roman",15,"bold"),bg="wheat4",fg="black",activebackground="wheat4").place(x=50,y=390,width=250,height=50)
b5 = Button(root,command=q,text="Borrow Chemicals",font = ("Times New Roman",15,"bold"),bg="wheat4",fg="black",activebackground="wheat4").place(x=50,y=480,width=250,height=50)
b6 = Button(root,command=p,text="Assign Project",font = ("Times New Roman",15,"bold"),bg="wheat4",fg="black",activebackground="wheat4").place(x=50,y=570,width=250,height=50)
root.mainloop()