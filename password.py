from tkinter import *

import random

win=Tk()
win.title("Random Password Generator")
win.geometry("500x500")
win.config(bg='cyan')

def password():
    s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"


    p="".join(random.sample(s,w.get()))
    
    password_display.config(text=p,font=("Arial Bold",15),bg='cyan',fg='blue') 
    



title=Label(win, text="Random Password Generator",font=("Arial Bold",25),bg='cyan')
title.pack(padx=20,pady=20)

length_display=Label(win, text="Select the length of the password",font=("Arial",15),bg='cyan')
length_display.pack()


w=IntVar()
length=Spinbox(win,from_=4,to_=15,textvariable=w)
length.pack(padx=20)

btn1=Button(win,text="Generate Password",bg='green',fg='white',command=password)
btn1.pack(padx=20,pady=20)

password_display=Label(win)
password_display.pack()

win.mainloop()
