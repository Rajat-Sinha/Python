#Creating a Status Bar
from tkinter import *

def doNothing():
    print('Do Nothing')
root = Tk()

# ***** Main Menu *****

menu = Menu(root)
root.config(menu=menu) #bsiclly config function config the menu to the root also put it to the top parameter=varible given from me

fileMenu = Menu(menu)
menu.add_cascade(label='File',menu=fileMenu) #adding label to the menu lso dding dropdown to the menu
fileMenu.add_command(label='New Project..',command=doNothing) #adding menu to the submenu
fileMenu.add_command(label='New..',command=doNothing) #adding menu to the submenu
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=root.quit)

editMenu = Menu(menu)
menu.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='Undo Typing',command=doNothing)

# ****** Toolbar ***********
toolbar = Frame(root,bg='grey')

insert_button = Button(toolbar,text='Insert',command=doNothing)
insert_button.pack(side=LEFT,padx=2,pady=2) #padx means padding in x direction
print_button = Button(toolbar,text='Print',command=doNothing)
print_button.pack(side=LEFT,padx=2,pady=2) #padx means padding in x direction

toolbar.pack(side=TOP,fil=X)

# ***** Status Bar *****
'''
bd means border
relief is anotner property of bd
anchor is positioning of label W for West
'''
status = Label(root,text='Preparing TO Do Nothing......',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()


