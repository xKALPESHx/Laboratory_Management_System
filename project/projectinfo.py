import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

r =tk.Tk()
r.title("Project Information")
r.geometry("1220x450+130+100")
r.configure(background="white")

connect = mysql.connector.connect(host="localhost",user="root",password="",database="lab",port="3306")

conn =connect.cursor()
conn.execute("SELECT * FROM project")

tree = ttk.Treeview(r)
tree['show']='headings'

s = ttk.Style(r)
s.theme_use("clam")

s.configure(".",font=("Times New Roman",12))
s.configure("Treeview.Heading",foreground="red",background='light steel blue',font=("Times New Roman",14))

tree["columns"] = ("pname","incharg","mem1","mem2","mem3","mem4","asdate","cdate")
tree.column("pname",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("incharg",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("mem1",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("mem2",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("mem3",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("mem4",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("asdate",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("cdate",width=150,minwidth=150,anchor=tk.CENTER)

tree.heading("pname",text="Project",anchor=tk.CENTER)
tree.heading("incharg",text="Incharge",anchor=tk.CENTER)
tree.heading("mem1",text="Member 1",anchor=tk.CENTER)
tree.heading("mem2",text="Member 2",anchor=tk.CENTER)
tree.heading("mem3",text="Member 3",anchor=tk.CENTER)
tree.heading("mem4",text="Member 4",anchor=tk.CENTER)
tree.heading("asdate",text="Assigned Date",anchor=tk.CENTER)
tree.heading("cdate",text="Completion Date",anchor=tk.CENTER)

i = 0
for ro in conn:
    tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7]))
    i = i + 1

vs = ttk.Scrollbar(r,orient="vertical")
vs.configure(command=tree.yview)
tree.configure(yscrollcommand=vs.set)
vs.pack(fill = Y, side = RIGHT)

tree.pack()

r.mainloop()