from tkinter import *

count = 0
def counter_label():
   global count
   count +=1

window = Tk()

window.title("GUI")


label = Label(window, text = "Hello everyone", fg = "dark green").pack()

#here I want to show the counter

label1 = Label(window, text=count).pack()

button = Button(window, text = "push",command = counter_label, fg = "blue", width = 10, height = 3, bg = "#fff").pack()

window.mainloop()