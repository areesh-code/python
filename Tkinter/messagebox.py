from tkinter import *

from tkinter import messagebox

root= Tk()

root.geometry("500x500")

def Danger():

    messagebox.showwarning("Alert", "Virus has been detected")

button=Button(text="Click Me", command=Danger)

button.place(x=9, y=4)

root.mainloop()