#Shapes and icon
from tkinter import *

root =Tk()
canvas = Canvas(root,width=200,height=100)
canvas.pack()
'''

'''
blackLine = canvas.create_line(0,0,200,50)  #(x,y)-initial  (x,y)-final
redLine = canvas.create_line(0,100,200,50,fill='red')
blueLine = canvas.create_line(100,100,200,50,fill='blue')
greenbox = canvas.create_rectangle(25,25,160,60,fill='green')#top,left,width,height

canvas.delete(blueLine) #All can be passed as parameter for deleting all the canvas

root.mainloop()