from tkinter import *
from tkinter import ttk

count = 0
def counter_label():
    global count

    label1.configure(text = f'button was clicked {count} times!!!')
    count += 1

window = Tk()

window.title("Button click")
label = Label(window, text = "Hello everyone")
label.grid(column = 0, row = 0)

#here I want to show the counter

label1 = Label(window)
label1.grid(column=0, row=1)

button = ttk.Button(window, text = "push",command = counter_label)
button.grid(column = 1, row =0 )

window.mainloop()