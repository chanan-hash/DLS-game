from tkinter import *

master = Tk()

def closewindow():
    exit()

button = Button(master, text = "close Window", command = closewindow)

# the pack() function - is tellig it just to put the thing somewhere in the window.
#there are all kind of functions that allow you to put the button where ever you want in the window

button.pack()

mainloop()