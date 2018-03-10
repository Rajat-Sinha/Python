#Fitting Widgets in a layout
from tkinter import *

root = Tk()

one = Label(root, text='ONE',fg='white',bg='black')
one.pack()
two = Label(root, text='TWO',fg='white',bg='red')
two.pack(fill=X) #fill = X means that if window sizes changes then the text size changes in x direction
three = Label(root, text='THREE',fg='white',bg='green')
three.pack(side=LEFT,fill=Y)



root.mainloop()