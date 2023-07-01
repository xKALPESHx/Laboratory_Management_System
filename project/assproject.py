from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import Tk
import mysql.connector
import os
#=======================================
root= Tk()
root.title("Assign Project")
root.geometry("405x630+630+50")
root.config(bg="light steel blue")
titel=Label(text="Assign Project",font=("Times New Roman",18,"bold"),bg="light steel blue",fg="black").place(x=120,y=10)
#=======================================
var_pn=StringVar()
var_ad=StringVar()
var_cd=StringVar()
#=======================================
L1 = Label(root,text = "Project Name:",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=20,y=60)
T1 = Entry(root,textvariable=var_pn,font = ("Times New Roman",13),bg="whitesmoke").place(x=190,y=60,width=200,height=25)

L2 = Label(root,text = "Project Incharg:",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=20,y=120)

L3 = Label(root,text = "Member 1:",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=20,y=180)

L4 = Label(root,text = "Member 2:",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=20,y=240)

L5 = Label(root,text = "Member 3:",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=20,y=300)

L6 = Label(root,text = "Member 4:",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=20,y=360)

L7 = Label(root,text = "Assinged Date:",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=20,y=420)
T3 = Entry(root,textvariable=var_ad,font = ("Times New Roman",13),bg="whitesmoke").place(x=190,y=420,width=200,height=25)

L8 = Label(root,text = "Complition Date:",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=20,y=480)
T4 = Entry(root,textvariable=var_cd,font = ("Times New Roman",13),bg="whitesmoke").place(x=190,y=480,width=200,height=25)

conn = mysql.connector.connect(user='root', password='',
                               host='localhost',
                               database='lab')
curs = conn.cursor()
curs.execute('select name from employe;')
results = curs.fetchall()
curs.close()
conn.close()

results_for_combobox = [result[0] for result in results]
comboBox = ttk.Combobox(root,state="readonly",values=results_for_combobox)
comboBox.place(x=190,y=120,width=200,height=25)
comboBox.current(0)

results_for_combobox1 = [result[0] for result in results]
comboBox1 = ttk.Combobox(root,state="readonly",values=results_for_combobox1)
comboBox1.place(x=190,y=180,width=200,height=25)
comboBox1.current(0)

results_for_combobox2 = [result[0] for result in results]
comboBox2 = ttk.Combobox(root,state="readonly",values=results_for_combobox2)
comboBox2.place(x=190,y=240,width=200,height=25)
comboBox2.current(0)

results_for_combobox3 = [result[0] for result in results]
comboBox3 = ttk.Combobox(root,state="readonly",values=results_for_combobox3)
comboBox3.place(x=190,y=300,width=200,height=25)
comboBox3.current(0)

results_for_combobox2 = [result[0] for result in results]
comboBox4 = ttk.Combobox(root,state="readonly",values=results_for_combobox2)
comboBox4.place(x=190,y=360,width=200,height=25)
comboBox4.current(0)

def buttonFunction():
    db=mysql.connector.connect(host="localhost",user="root",password="",database="lab")
    command_handler=db.cursor()
    command_handler.execute("insert into project values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                var_pn.get(),
                                                                comboBox.get(),
                                                                comboBox1.get(),
                                                                comboBox2.get(),
                                                                comboBox3.get(),
                                                                comboBox4.get(),
                                                                var_ad.get(),
                                                                var_cd.get()
                                                                ))
    db.commit()
    db.close()
    messagebox.showinfo("Sucsses","Entry Recorded")
    
bt=Button(root, text="Assign",cursor="hand2",command=buttonFunction,font=("Times New Roman",15),bg="wheat4",fg="blue").place(x=140,y=570,width=100,height=30)



root.mainloop()