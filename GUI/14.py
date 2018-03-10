#Images and Icon
from tkinter import *

root = Tk()

photo = PhotoImage(file="achiredo.png")
label = Label(root,image=photo)
label.pack()

root.mainloop()

