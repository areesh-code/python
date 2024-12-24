from tkinter import *
window=Tk()
window.title("Tkinter Window")
window.geometry("500x500")
m=Label(text="Enter Name", bg="Red", fg="Orange")
m.pack()
n=Entry()
n.pack()
k=Button(text="Click Me", bg="black", fg="yellow")
k.pack()
v=Frame(master=window,relief=RAISED)
v.pack()
b=Label(master=v,text="Label on frame")
b.pack()
window.mainloop()


