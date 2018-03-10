#GRId Layout
from tkinter import *
root = Tk()

label1 = Label(root,text='Name')
label2 = Label(root,text='Password')
entry1 = Entry(root) #This function is basically used for the input from user
entry2 = Entry(root)

'''
grid function is used for making row and column set instead of using pack function
by default row=0,column=0
grid(row=n,column=n,sticky=)
sticky takes N,S,E,W N for North
'''

label1.grid(row=0,sticky=E)
label2.grid(row=1)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

c = Checkbutton(root, text='Keep Me Loggedin')
c.grid(columnspan=2)

root.mainloop()