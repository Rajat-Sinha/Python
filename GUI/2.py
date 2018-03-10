#Organising Layout
from tkinter import *

root = Tk()

topFrame = Frame(root)#invisible container that gonna in a main window
topFrame.pack() #for displaying in a main window
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM) #display frame in the bottom of the main Window

'''
Button function is used for making button 
Takes Three Parameter
1=inwhich frame dows you want to put the button
2=what text you want ot display on button
3=color of the button
'''
button1 = Button(topFrame,text='Button 1',fg='red')
button2 = Button(topFrame,text='Button 2',fg='purple')
button3 = Button(topFrame,text='Button 3',fg='green')
button4 = Button(bottomFrame,text='Button 4',fg='blue')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()