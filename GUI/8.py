#Using Classess

from tkinter import *

'''
master must be passe to  the __init__ function in cse of GUI
master bsically nother terms used for root
frame.quit is bsiclly  builtin function for breking the mainloop or closing the window
'''

class MyButton:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text='Print The Message',command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame,text='Quit',command=frame.quit)
        self.quitButton.pack(side=RIGHT)
    def printMessage(self):
        print('Wow! It Worked')

root = Tk()
m = MyButton(root)
root.mainloop()

