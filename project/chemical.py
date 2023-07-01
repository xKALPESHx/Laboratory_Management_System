from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import os

root= Tk()
#=====phase1====
root.title("Chemicals Transaction")
root.geometry("750x450+500+150")
var_dod=StringVar()
var_quantity=StringVar()
var_payment=StringVar()
root.config(bg="light steel blue")
titel=Label(text="Purchased Chemicals",font=("times new roman",20,"bold"),bg="light steel blue",fg="black").place(x=420,y=10)
root.left=ImageTk.PhotoImage(file="C:/Users/KalKun/Desktop/Sem-4 Mini Project/Images/t.jpg")
left=Label(root,image=root.left).place(x=0,y=0,width=350,height=550)
#=====phase2=====
chemical=["Acetic Acid","Formic Acid","Hydrocloric Acid","Hydrofluoric Acid","Nitric Acid", "Sulfuric Acide","Ammonium Hydroxide","Sodium Hydroxide","Preclioric Acid"]

l1=Label(root,text="Select Stock:",font=("times new roman",15,"bold"),bg="light steel blue",fg="black").place(x=370,y=70)
cb1 = ttk.Combobox(root,font = ("times new roman",10),state = "readonly")
cb1["values"]=("Acetic Acid","Formic Acid","Hydrocloric Acid","Hydrofluoric Acid","Nitric Acid", "Sulfuric Acide","Ammonium Hydroxide","Sodium Hydroxide","Preclioric Acid")
cb1.place(x=570,y=75,width=150,height=25)
cb1.current(0)

l2=Label(text="Transaction Date:",font=("times new roman",15,"bold"),bg="light steel blue",fg="black").place(x=370,y=120)
txt_l2=Entry(textvariable=var_dod,font=("times new roman",15,),bd=2).place(x=570,y=125,width=150)

l3=Label(text="State:",font=("times new roman",15,"bold"),bg="light steel blue",fg="black").place(x=370,y=175)
cb = ttk.Combobox(root,font = ("times new roman",10),state = "readonly")
cb["values"]=("Solid","Liquid","Gas")
cb.place(x=570,y=175,width=150,height=25)
cb.current(0)

l4=Label(text="Quantity :",font=("times new roman",15,"bold"),bg="light steel blue",fg="black").place(x=370,y=230)
txt_l4=Entry(textvariable=var_quantity,font=("times new roman",15),bd=2).place(x=570,y=235,width=150)

l5=Label(text="Total Cost:",font=("times new roman",15,"bold"),bg="light steel blue",fg="black").place(x=370,y=280)
txt_l5=Entry(textvariable=var_payment,font=("times new roman",15),bd=2).place(x=570,y=285,width=150)

#=====phase4=====
def buttonFunction():
    db=mysql.connector.connect(host="localhost",user="root",password="",database="lab")
    command_handler=db.cursor()
    command_handler.execute("insert into cm values(%s,%s,%s,%s,%s)",(
                                                                cb1.get(),
                                                                var_dod.get(),
                                                                cb.get(),
                                                                var_quantity.get(),
                                                                var_payment.get()
                                                                ))
    db.commit()
    db.close()
    messagebox.showinfo("Entry Recorded",parent=root)
    print("Success","Entry Recorded")
bt=Button(root, text="Save",cursor="hand2",command=buttonFunction,font=("times new roman",15),bg="wheat4",fg="blue").place(x=500,y=390,width=100,height=30)


root.mainloop()