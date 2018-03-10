#Messagebox
from tkinter import *
import tkinter.messagebox #for using messagebox

root = Tk()

#tkinter.messagebox.showinfo('Window Title','Window Body')

answer = tkinter.messagebox.askquestion('Question 1','Do you like me?')

if answer == 'yes':
    tkinter.messagebox.showinfo('Window Title', 'Answered Yes')

root.mainloop()
