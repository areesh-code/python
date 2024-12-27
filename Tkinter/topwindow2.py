from tkinter import *
from PIL import Image, ImageTk
window=Tk()
window.geometry("500x500")
upload=Image.open("R.jpg")
image=ImageTk.PhotoImage(upload)
label= Label(image=image, height=400, width=300)
label.pack()
window.mainloop()