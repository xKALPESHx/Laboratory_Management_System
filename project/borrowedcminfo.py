import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

r =tk.Tk()
r.title("Chemical Information")
r.geometry("770x450+330+100")
r.configure(background="white")

connect = mysql.connector.connect(host="localhost",user="root",password="",database="lab",port="3306")

conn =connect.cursor()
conn.execute("SELECT * FROM b2")

tree = ttk.Treeview(r)
tree['show']='headings'

s = ttk.Style(r)
s.theme_use("clam")

s.configure(".",font=("Times New Roman",12))
s.configure("Treeview.Heading",foreground="red",background='light steel blue',font=("Times New Roman",14))

tree["columns"] = ("Chemical","name","date","state","quantity")
tree.column("Chemical",width=200,minwidth=200,anchor=tk.CENTER)
tree.column("name",width=250,minwidth=250,anchor=tk.CENTER)
tree.column("date",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("state",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("quantity",width=100,minwidth=100,anchor=tk.CENTER)

tree.heading("Chemical",text="Chemical",anchor=tk.CENTER)
tree.heading("name",text="Name of Borrower",anchor=tk.CENTER)
tree.heading("date",text="Date",anchor=tk.CENTER)
tree.heading("state",text="State",anchor=tk.CENTER)
tree.heading("quantity",text="Quantity",anchor=tk.CENTER)

i = 0
for ro in conn:
    tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
    i = i + 1

vs = ttk.Scrollbar(r,orient="vertical")
vs.configure(command=tree.yview)
tree.configure(yscrollcommand=vs.set)
vs.pack(fill = Y, side = RIGHT)

tree.pack()

r.mainloop()