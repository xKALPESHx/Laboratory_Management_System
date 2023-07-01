from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import Tk
import mysql.connector
import random
import os
#=======================================
root= Tk()
root.title("Registration Page")
root.geometry("730x500+470+100")
root.config(bg="light steel blue")
titel=Label(text="Employee Registration",font=("Times New Roman",18,"bold"),bg="light steel blue",fg="black").place(x=240,y=10)
#=======================================
var_ref=StringVar()
x=random.randint(100,1000)
var_ref.set(str(x))
#=======================================
var_nam=StringVar()
var_email=StringVar()
var_phone=StringVar()
var_sal=StringVar()
var_dob=StringVar()
var_add=StringVar()
#=======================================
L1 = Label(root,text = "Full Name",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=20,y=60,width=100,height=20)
T1 = Entry(root,textvariabl=var_nam,font = ("Times New Roman",13),bg="whitesmoke").place(x=150,y=60,width=200,height=20)

L2 = Label(root,text = "Email ID",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=20,y=110,width=100,height=20)
T2 = Entry(root,textvariabl=var_email,font = ("Times New Roman",13),bg="whitesmoke").place(x=150,y=110,width=200,height=20)

L3 = Label(root,text = "Phone No",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=20,y=160,width=100,height=20)
T3 = Entry(root,textvariabl=var_phone,font = ("Times New Roman",13),bg="whitesmoke").place(x=150,y=160,width=200,height=20)

L4 = Label(root,text = "Post",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=20,y=210,width=100,height=20)
cb1 = ttk.Combobox(root,font = ("Times New Roman",11),state = "readonly")
cb1["values"]=("Employee","Manager","Assistant","Researcher")
cb1.place(x=150,y=210,width=200,height=20)
cb1.current(0)

L5 = Label(root,text = "Address",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=370,y=210,width=100,height=20)
T4 = Entry(root,textvariabl=var_add,font = ("Times New Roman",13),bg="whitesmoke").place(x=500,y=210,width=200,height=20)

L7 = Label(root,text = "Salary",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=20,y=260,width=110,height=20)
T5 = Entry(root,textvariabl=var_sal,font = ("Times New Roman",13,),bg="whitesmoke").place(x=150,y=260,width=200,height=20)

L8 = Label(root,text = "City",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=370,y=260,width=100,height=20)
cb2 = ttk.Combobox(root,font = ("Times New Roman",11),state="readonly")
cb2["values"]=("Mumbai","Pune","Thane","Kolkata","Chennai","Banglore","Delhi","Surat")
cb2.place(x=500,y=260,width=200,height=20)
cb2.current(0)

L9 = Label(root,text = "Gender",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=370,y=60,width=100,height=20)    
cc2 = ttk.Combobox(root,font = ("Times New Roman",11),state="readonly")
cc2["values"]=("Male","Female")
cc2.place(x=500,y=60,width=200,height=20)
cc2.current(0)

L10 = Label(root,text = "Employee ID",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=370,y=110,width=122,height=20)
T6 = Entry(root,textvariabl=var_ref,font = ("Times New Roman",13),bg="whitesmoke",state="readonly").place(x=500,y=110,width=200,height=20)

L11 = Label(root,text = "Date of Birth",anchor="w",font = ("Times New Roman",14,"bold"),bg='light steel blue',fg="black").place(x=370,y=160,width=120,height=20)
T7 = Entry(root,textvariabl=var_dob,font = ("heletica",13),bg="whitesmoke").place(x=500,y=160,width=200,height=20)
#==========================================
def buttonFunction():
    if var_nam.get()=="" or var_email.get()=="" or var_phone.get()=="" or cb1.get()=="" or var_add.get()=="" or var_sal.get()=="" or cb2.get()=="" or cc2.get()=="" or var_dob.get()=="":
     messagebox.showerror("Incomplete Information","Fill all of the required details")
    else:
     db=mysql.connector.connect(host="localhost",user="root",password="",database="lab")
     command_handler=db.cursor()
     command_handler.execute("insert into employe values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                             var_nam.get(),
                                                                                             var_email.get(),
                                                                                             var_phone.get(),
                                                                                             cb1.get(),
                                                                                             var_add.get(),
                                                                                             var_sal.get(),
                                                                                             cb2.get(),
                                                                                             cc2.get(),
                                                                                             var_ref.get(),
                                                                                             var_dob.get(),                                                                       
     ))
     db.commit()
     messagebox.showinfo("Success","Registation Successful")

b1 = Button(root,command=buttonFunction,text="Register",cursor="hand2",font = ("Times New Roman",16,"bold"),bd=3,relief="raised",bg="firebrick4",fg="white",activebackground="firebrick4",activeforeground="black").place(x=300,y=390,width=120,height=30)
root.mainloop()