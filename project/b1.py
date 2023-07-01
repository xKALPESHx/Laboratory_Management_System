from tkinter import*
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector 
import os
#=======================================================
root= Tk()
root.title("Borrow Apparatus")
root.geometry("750x450+500+150")
var_en=StringVar()
var_bd=StringVar()
var_qt=StringVar()

root.config(bg="light steel blue")
titel=Label(text="Borrow Apparatus",font=("Times New Roman",20,"bold"),bg="light steel blue",fg="black").place(x=430,y=10)
root.left=ImageTk.PhotoImage(file="image/co.jpg")
left=Label(root,image=root.left).place(x=0,y=0,width=350,height=450)
#======================================================
l1=Label(root,text="Select Apparatus:",font=("Times New Roman",15,"bold"),bg="light steel blue",fg="black").place(x=370,y=60)
cb1 = ttk.Combobox(root,font = ("Times New Roman",10),state = "readonly")
cb1["values"]=("Test-tube","conical Flask","Buret","Beaker","Thermometer","Funnel","Burner","Florence Flask","Erienmeyer Flask")
cb1.place(x=570,y=65,width=150,height=25)
cb1.current(0)

l2=Label(text="Employee Name:",font=("Times New Roman",15,"bold"),bg="light steel blue",fg="black").place(x=370,y=120)

l3=Label(text="Borrowed Date:",font=("Times New Roman",15,"bold"),bg="light steel blue",fg="black").place(x=370,y=175)
t3= Entry(textvariable=var_bd,font=("Times New Roman",15,),bd=2).place(x=570,y=175,width=150)

l4=Label(text="Apparatus size:",font=("Times New Roman",15,"bold"),bg="light steel blue",fg="black").place(x=370,y=230)
cb = ttk.Combobox(root,font = ("Times New Roman",10),state = "readonly")
cb["values"]=("Small","Medium","Large")
cb.place(x=570,y=235,width=150,height=25)
cb.current(0)

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
comboBox.place(x=570,y=125,width=150,height=25)
comboBox.current(0)

def buttonFunction():
    db=mysql.connector.connect(host="localhost",user="root",password="",database="lab")
    command_handler=db.cursor()
    command_handler.execute("insert into b1 values(%s,%s,%s,%s,%s)",(
                                                                cb1.get(),
                                                                var_en.get(),
                                                                cb.get(),
                                                                var_bd.get(),
                                                                var_qt.get()
                                                                ))
    db.commit()
    db.close()
    messagebox.showinfo("Sucsses","Entry Recorded")
    
bt=Button(root, text="Save",cursor="hand2",command=buttonFunction,font=("Times New Roman",15),bg="wheat4",fg="blue").place(x=500,y=390,width=100,height=30)



l5=Label(text="Quantity:",font=("Times New Roman",15,"bold"),bg="light steel blue",fg="black").place(x=370,y=280)
tex3= Entry(textvariable=var_qt,font=("Times New Roman",15),bd=2).place(x=570,y=285,width=150)




root.mainloop()
