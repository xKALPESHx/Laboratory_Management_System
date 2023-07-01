from tkinter import*
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector 
import random
import os
#====================================
root= Tk()
root.title("New Manager Registration")
root.geometry("1350x700+0+0")
 #=================================
var_ref=StringVar()
x=random.randint(1000,9999)
var_ref.set(str(x))
#==================================
var_f=StringVar()
var_l=StringVar()
var_u=StringVar()
var_p=StringVar()
var_cp=StringVar()
#==================================
root.bg=ImageTk.PhotoImage(file="image/wall2.jpg")
bg=Label(root,image=root.bg).place(x=0,y=0,relwidth=1,relheight=1)

root.left=ImageTk.PhotoImage(file="image/co.jpg")
left=Label(root,image=root.left).place(x=80,y=100,width=400,height=500)

frame=Frame(root,bg='white')
frame.place(x=480,y=100,width=800,height=500)
#===================================
titel=Label(frame,text="NEW MANAGER REGISTRATION",font=("helvetica",20,"bold"),bg="white",fg="blue").place(x=50,y=30)

l1=Label(frame,text="First Name :",font=("helvetica",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
t1=Entry(frame,textvariabl=var_f,font=("helvetica",15),bg="light gray").place(x=50,y=130,width=250)

l2=Label(frame,text="Last Name :",font=("helvetica",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
t2=Entry(frame,textvariabl=var_l,font=("helvetica",15),bg="light gray").place(x=370,y=130,width=250)

l3=Label(frame,text="Username :",font=("helvetica",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
t3=Entry(frame,textvariabl=var_u,font=("helvetica",15),bg="light gray").place(x=50,y=200,width=250)

l4=Label(frame,text="Password :",font=("helvetica",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
t4=Entry(frame,textvariabl=var_p,font=("helvetica",15),bg="light gray").place(x=370,y=200,width=250)

l5=Label(frame,text = "Manger ID :",anchor="w",font = ("helvetica",14,"bold"),bg='white',fg="gray").place(x=50,y=240)
t5=Entry(frame,textvariabl=var_ref,font = ("helvetica",13),bg="gray",state="readonly").place(x=50,y=270,width=250)

l4=Label(frame,text="Confirm Password :",font=("helvetica",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
t4=Entry(frame,textvariabl=var_cp,font=("helvetica",15),bg="light gray").place(x=370,y=270,width=250)
#=======================================
def cb():
        f='login.py'
        os.system(f)
def buttonFunction():
    if var_f.get()=="" or var_l.get()=="" or var_u.get()=="" or var_p.get()=="" or var_cp.get()=="":
        messagebox.showerror("Incomplete Information","Fill all of the required details")
    elif var_p.get()!=var_cp.get():
        messagebox.showerror("Error","Password & Confirm password must be same")
    else:
     db=mysql.connector.connect(host="localhost",user="root",password="",database="lab")
     command_handler=db.cursor()
     query=("select * from manger where user=%s")
     value=(var_u.get(),)
     command_handler.execute(query,value)
     row=command_handler.fetchone()
    if row!=None:
     messagebox.showerror("Error","User alredy exist")
    else:
     command_handler.execute("insert into manger values(%s,%s,%s,%s,%s,%s)",(
                                                                              var_f.get(),
                                                                              var_l.get(),
                                                                              var_u.get(),
                                                                              var_p.get(),
                                                                              var_cp.get(),
                                                                              var_ref.get(),
     ))
     db.commit()
     db.close()
     messagebox.showinfo("Sucsses","New Maneger Registerd")
bt=Button(frame,command=buttonFunction, text="Save",cursor="hand2",font=("helvetica",15,"bold"),bg="sky blue").place(x=300,y=380,width=100,height=30)
b2 = Button(frame,command=cb,text="Return to Sign In",font = ("helvetica",12),borderwidth=0,bg="White",fg="blue",activebackground="light steel blue").place(x=290,y=430,width=120,height=20)

root.mainloop()