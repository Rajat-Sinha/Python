#Threading

import threading

class Messenger(threading.Thread): #module.classname
    def run(self):
        for _ in range(10):#_ is for assuming any variables
            print(threading.current_thread().getName())

x = Messenger(name='Sending out the messages')
y = Messenger(name='Receiving the messages')

#to start thread we have to use start function and it will automatically call the run function in the class
x.start()
y.start()
