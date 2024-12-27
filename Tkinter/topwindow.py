from tkinter import *
window=Tk()
window.title("Main Window")
window.geometry("500x500")
window.configure(bg="lightblue")
def fun():
    window2=Toplevel()
    window2.title("Second Window")
    window2.geometry("400x400")
    window2.configure(bg="Red")

    window2.mainloop()

b=Button(window, text="Click me", command=fun)

b.pack()

window.mainloop()
