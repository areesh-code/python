from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("Money Calculater")
root.geometry("650x400")
root.configure(bg= "Orange")
upload=Image.open("Money.jpg")
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(root, image=image)
label.place(x=20,y=12)
label2=Label(root, text="Welcome to my application")
label2.place(x=50, y=355)
def msg():
    msgbox=messagebox.showinfo("Caculator", "Would you like to caculate the amount of your money")
    if msgbox=="ok":
        topwin()
button=Button(text="Calculate", command=msg)
button.place(x=50, y=365)
def topwin():
    top= Toplevel()
    top.title("Calculation")
    top.geometry("600x350+50+50")
    top.configure(bg= "Blue")
    label3=Label(top, text="Enter the amount of money")
    entry=Entry(top)
    l1=Label(top, text="2000")
    l2=Label(top, text="500")
    l3=Label(top, text="100")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    def calculator():
        global amount
        amount= int(entry.get())
        amount2000=amount//2000
        amount=amount%2000

        amount500=amount//500
        amount=amount%500

        amount100=amount//100
        amount=amount%100
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
        t1.insert(END, str(amount2000))
        t2.insert(END, str(amount500))
        t3.insert(END, str(amount100))
    button1=Button(top, text="Caculate",command=calculator)
    label3.place(x=230, y=50)
    entry.place(x=200, y=80)
    button1.place(x=240, y=100)
    l1.place(x=180, y=200)
    l2.place(x=180, y=240)
    l3.place(x=180, y=260)
    t1.place(x=270, y=200)
    t2.place(x=270, y=240)
    t3.place(x=270, y=260)
    top.mainloop()
root.mainloop()