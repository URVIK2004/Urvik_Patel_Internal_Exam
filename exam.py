
import functools
from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox


root = Tk()  
root.geometry("500x500")  
root.title(" List Box") 
root.config(background="light blue")
list=Listbox(height=5,width=50)

lb1= Label(root, text="First Name", width=15, font=("arial",12))  
lb1.place(x=20, y=200)  
en1= Entry(root)  
en1.place(x=200, y=200)

lb2= Label(root, text="last Name", width=15, font=("arial",12))  
lb2.place(x=20, y=250)  
en2= Entry(root)  
en2.place(x=200, y=250)


lb3= Label(root, text="Gender", width=15, font=("arial",12))  
lb3.place(x=20, y=300)  
vars = IntVar()  
Radiobutton(root, text="Male", padx=5,variable=vars, value=1).place(x=200, y=300)  
Radiobutton(root, text="Female", padx =10,variable=vars, value=2).place(x=300,y=300)  

lb4= Label(root, text="Languages", width=15, font=("arial",12))  
lb4.place(x=20, y=350)  
vars = IntVar() 
Checkbutton1 = tkinter.IntVar()
Checkbutton2 = tkinter.IntVar() 
Checkbutton3 = tkinter.IntVar()
Button1 = Checkbutton(root, text = "Telugu",padx=20, variable = Checkbutton1,onvalue = 1, offvalue = 0).place(x=200, y=350) 
Button2 = Checkbutton(root, text = "English",padx=20, variable = Checkbutton2,onvalue = 1, offvalue = 0).place(x=300, y=350) 
Button3 = Checkbutton (root, text = "Hindi", padx=20,variable = Checkbutton3,onvalue = 1,offvalue = 0,).place(x=400, y=350) 
 
lb5= Label(root, text="Email", width=15, font=("arial",12))  
lb5.place(x=20, y=400)  
en5= Entry(root)  
en5.place(x=200, y=400)

lb6= Label(root, text="Address", width=15, font=("arial",12))  
lb6.place(x=20, y=450)  
en6= Entry(root)  
en6.place(x=200, y=450)

lb7= Label(root, text="State", width=15, font=("arial",12))  
lb7.place(x=20, y=500)  
var = StringVar()
var.set("Chooes state")
data=("jaipur", "Delhi", "ahmedabad", "surat")
cb=Combobox(root, values=data)
cb.place(x=200, y=500)

lb8= Label(root, text="Zip", width=15, font=("arial",12))  
lb8.place(x=20, y=550)  
en8= Entry(root)  
en8.place(x=200, y=550)

lb9= Label(root, text="Cradit Card Type", width=15, font=("arial",12))  
lb9.place(x=20, y=600)  
var = StringVar()
var.set("Chooes state")
data=("SBI","ICICI","BOI")
cb=Combobox(root, values=data)
cb.place(x=200, y=600)

lb10 = Listbox(root,x=1200,y=900,height=20,width=90)
l = Label(root,text = "Bellings Record")
lb10.place(x=200, y=200)
l.pack()
lb10.pack()

b1 = Button(root,text = "insert",command = functools,pady=10,padx=20)
b1.pack()
b1.place(x=600, y=200) 
def fun():
     messagebox.showinfo( "insert")

b2 = Button(root,text = "Delete",command = functools,pady=10,padx=20)
b2.pack()
b2.place(x=600, y=300) 
def fun():
     messagebox.showinfo( "Delete")
     
b3 = Button(root,text = "Theam",command = functools,pady=10,padx=20)
b3.pack()
b3.place(x=600, y=400) 
def fun():
     messagebox.showinfo( "Theam")

root.mainloop()