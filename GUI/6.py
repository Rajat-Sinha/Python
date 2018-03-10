#Binding Function TO the Layout
from tkinter import *

root = Tk()
def printName(event):
    print('Hello My Name is Rajat')

#button1 = Button(root, text='Click Me!!',command=printName)
button1 = Button(root, text='Click Me!!')
button1.bind('<Button-1>',printName) #<Button-1> is the left click of the mouse button
'''
bind function is used for binding the button with the fucntion you want ot run after clicking the button
'''

button1.pack()

root.mainloop()

