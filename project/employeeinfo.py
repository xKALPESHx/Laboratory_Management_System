import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

r =tk.Tk()
r.title("name Information")
r.geometry("1210x450+150+100")
r.configure(background="white")

connect = mysql.connector.connect(host="localhost",user="root",password="",database="lab",port="3306")

conn =connect.cursor()
conn.execute("SELECT * FROM employe")

tree = ttk.Treeview(r)
tree['show']='headings'

s = ttk.Style(r)
s.theme_use("clam")

s.configure(".",font=("Times New Roman",12))
s.configure("Treeview.Heading",foreground="red",background='light steel blue',font=("Times New Roman",14))

tree["columns"] = ("name","email","phone","post","addresse","salary","city","gender","id","dob")
tree.column("name",width=250,minwidth=250,anchor=tk.CENTER)
tree.column("email",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("phone",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("post",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("addresse",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("salary",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("city",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("gender",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("id",width=120,minwidth=120,anchor=tk.CENTER)
tree.column("dob",width=120,minwidth=120,anchor=tk.CENTER)

tree.heading("name",text="Name",anchor=tk.CENTER)
tree.heading("email",text="Email ID",anchor=tk.CENTER)
tree.heading("phone",text="Phone NO",anchor=tk.CENTER)
tree.heading("post",text="Post",anchor=tk.CENTER)
tree.heading("addresse",text="Address",anchor=tk.CENTER)
tree.heading("salary",text="Salary",anchor=tk.CENTER)
tree.heading("city",text="City",anchor=tk.CENTER)
tree.heading("gender",text="Gender",anchor=tk.CENTER)
tree.heading("id",text="Employee ID",anchor=tk.CENTER)
tree.heading("dob",text="Date of Birth",anchor=tk.CENTER)

i = 0
for ro in conn:
    tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9]))
    i = i + 1

vs = ttk.Scrollbar(r,orient="vertical")
vs.configure(command=tree.yview)
tree.configure(yscrollcommand=vs.set)
vs.pack(fill = Y, side = RIGHT)

tree.pack()

r.mainloop()