import tkinter as tk
from tkinter import*
from tkinter import ttk
import os

f = tk.Tk()
f.title("Laboratory System Dashboard")
f.geometry("1530x800+-10+0")
def c():
        f='input.py'
        os.system(f)

def b():
        f='database.py'
        os.system(f)
b1 = Button(f,command=c,text="Data Entry",font = ("times new roman",40,"bold"),bd=3,relief="raised",bg="sky blue",fg="red",activebackground="sky blue",activeforeground="black")
b1.place(x=20,y=10,width=660,height=710)

b2 = Button(f,command=b,text="Display Data",font = ("times new roman",40,"bold"),bd=3,relief="raised",bg="light green",fg="red",activebackground="light green",activeforeground="black")
b2.place(x=690,y=10,width=660,height=710)

f.mainloop()