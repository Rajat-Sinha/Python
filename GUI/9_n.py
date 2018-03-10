#creting Dropdown Menus


from tkinter import *

def doNothing():
    print('Do Nothing')
root = Tk()

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

root.mainloop()


