from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import Tk
import mysql.connector
import os
#=======================================
root= Tk()
root.title("DATABASE")
root.geometry("1530x800+-10+0")
root.config(bg="light steel blue")
titel=Label(text="Database",font=("Times New Roman",30,"bold"),bg="light steel blue",fg="black").place(x=500,y=10,width=500)

def c():
        f='employeeinfo.py'
        os.system(f)
def b():
        f='apparatusinfo.py'
        os.system(f)
def d():
        f='cheminfo.py'
        os.system(f)
def a():
        f='borrowedapinfo.py'
        os.system(f)
def q():
        f='borrowedcminfo.py'
        os.system(f)
def p():
        f='projectinfo.py'
        os.system(f)

b2 = Button(root,command=c,text="Employee Data",font = ("Times New Roman",12,"bold"),bg="wheat4",fg="black",activebackground="wheat4").place(x=50,y=100,width=250,height=50)
b2 = Button(root,command=b,text="Apparatus Data",font = ("Times New Roman",12,"bold"),bg="wheat4",fg="black",activebackground="wheat4").place(x=50,y=190,width=250,height=50)
b2 = Button(root,command=d,text="Chemicals Data",font = ("Times New Roman",12,"bold"),bg="wheat4",fg="black",activebackground="wheat4").place(x=50,y=280,width=250,height=50)
b2 = Button(root,command=a,text="Borrowed Apparatus",font = ("Times New Roman",12,"bold"),bg="wheat4",fg="black",activebackground="wheat4").place(x=50,y=370,width=250,height=50)
b2 = Button(root,command=q,text="Borrowed Chemicals",font = ("Times New Roman",12,"bold"),bg="wheat4",fg="black",activebackground="wheat4").place(x=50,y=460,width=250,height=50)
b5 = Button(root,command=p,text="Project data",font = ("Times New Roman",12,"bold"),bg="wheat4",fg="black",activebackground="wheat4").place(x=50,y=550,width=250,height=50)

root.mainloop()