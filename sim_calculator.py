import math
import tkinter as tk
from tkinter import*

root=Tk()

root.geometry("400x550")
root.title("Simple Calculator")


cal=StringVar()
cal.set("")
display=Entry(root,textvar=cal,font="Calibri 30",background="yellow")
display.pack(fill=X,  ipadx=6 ,ipady=6)

frame1=Frame(root)
button=Button(frame1,text="9",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT)
frame1.pack()

button=Button(frame1,text="8",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=RIGHT)

button=Button(frame1,text="7",font="Calibri 18",padx=22,pady=20,background="light gray")
button.pack(side=LEFT)



root.mainloop()