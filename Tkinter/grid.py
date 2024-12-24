from tkinter import *
window=Tk()
window.title("Grid System")
window.geometry("500x500")
for i in range(3):
  for j in range(3):
    frame=Frame(window,relief=RAISED,borderwidth=1)
    frame.grid(row=i,column=j, padx=5,pady=5)
    label=Label(frame,text=[i,j], width=10, height=5)
    label.pack()
window.mainloop()