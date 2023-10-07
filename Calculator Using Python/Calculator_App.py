import tkinter
from tkinter import *

root=Tk() #To create a main window
root.title("Calculator") #Title of the window
root.geometry("570x600+800+100") #size of the window
root.resizable(False,False) #window is resizable or not
root.configure(bg="#9FBEE3")#Background color

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation,fg="#1F4172")

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if(equation!=""):
        try:
            result=eval(equation)
        except:
            result="Error"
            equation=""
    if result=="Error":
        label_result.config(fg="#C84B31")
    label_result.config(text=result)

logo = PhotoImage(file = 'calc_logo.png')
root.iconphoto(False, logo) 

label_result=Label(root,width=25,height=2,text="",fg="#1F4172",bg="#BCD8F9",font=("arial",30,"bold"))
label_result.pack()

Button(root,text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#FF6969",command=lambda: clear()).place(x=10,y=110)
Button(root,text="(",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#E6B325",command=lambda: show("(")).place(x=150,y=110)
Button(root,text=")",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#E6B325",command=lambda: show(")")).place(x=290,y=110)
Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#E6B325",command=lambda: show("/")).place(x=430,y=110)

Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#3085C3",command=lambda: show("7")).place(x=10,y=210)
Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#3085C3",command=lambda: show("8")).place(x=150,y=210)
Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#3085C3",command=lambda: show("9")).place(x=290,y=210)
Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#E6B325",command=lambda: show("*")).place(x=430,y=210)

Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#3085C3",command=lambda: show("4")).place(x=10,y=310)
Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#3085C3",command=lambda: show("5")).place(x=150,y=310)
Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#3085C3",command=lambda: show("6")).place(x=290,y=310)
Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#E6B325",command=lambda: show("-")).place(x=430,y=310)

Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#3085C3",command=lambda: show("1")).place(x=10,y=410)
Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#3085C3",command=lambda: show("2")).place(x=150,y=410)
Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#3085C3",command=lambda: show("3")).place(x=290,y=410)
Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#E6B325",command=lambda: show("+")).place(x=430,y=410)

Button(root,text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#3085C3",command=lambda: show("0")).place(x=10,y=510)
Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#3085C3",command=lambda: show(".")).place(x=290,y=510)
Button(root,text="=",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#54B435",command=lambda: calculate()).place(x=430,y=510)

root.mainloop()

