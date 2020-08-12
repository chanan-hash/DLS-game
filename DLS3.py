from tkinter import *
from tkinter import ttk, messagebox
import random

#creat the window

root = Tk()
root.title ("Defened Load Shoot !!")

# here we can put an icon' but we mut jave it in pur folder
#root.iconbitmap(r'rock_vEL_icon.ico')


label = Label(root, text = "Defened Load Shoot !!" ).pack()
#label.grid(row = 0, column = 1)

root.resizable(width=False, height=False)

#the variable who runs the game
click = True

# the stack and counters

yourStack = 0
comStack = 0
countWin = 0
countLose = 0

# the buttons
buttonD = ''
buttonL = ''
buttonS = ''

def play():
    global buttonD,buttonL,buttonS

    buttonD = ttk.Button(text = "Defense", command = lambda: youPick('defense')).pack()
    buttonL = ttk.Button(text = "Load", command = lambda: youPick('load')).pack()
    buttonS = ttk.Button(text = "Shoot", command = lambda: youPick('shoot')).pack()

#    buttonD.grid(row = 1, column = 0)
 #   buttonL.grid(row = 1, column = 1)
  #  buttonS.grid(row = 1, column = 2)

def computerPick():
    global comStack
    if comStack == 0:
        return random.choice(['defense', 'load'])
    else:
        return random.choice(['defense','load','shoot'])


# the game itself
def youPick(yourChoise):
    global click,countLose,countWin,comStack,yourStack
    compPick = computerPick()

# the loading
    if click == True:

        if yourChoise == 'load':
            yourStack +=1
            click = False
        if compPick == 'load':
            comStack +=1

        #if yourChoise == 'shoot':
         #   yourStack -=1
        #if comStack == 'shoot':
          #  comStack -=1

# if you don't have any bullets
        while yourStack == 0:
            if yourChoise == 'shoot':
                messagebox.showinfo("mach","you don't have any bullets, you must load before")
                compPick = 0
                click = False
                break
            elif yourChoise == 'defense':
                continue

        if yourStack > 0 or comStack >0:
#load
            if yourChoise == 'load' and compPick == 'defense':
                click = False
                print("The Computer chose: ",compPick,"Keep playing")
                messagebox.showinfo("mach",f"The computer chose: {compPick}. Keep playing")
            elif yourChoise == 'load' and compPick == 'shoot':
                comStack -=1
                countLose +=1
                click = False
                print("The Computer chose: ",compPick,"He shot you, you lost this roud ):")
                messagebox.showinfo("mach",f"The computer chose: {compPick}. He shot you, you lost this roud ):")
#defense
            elif yourChoise == 'defense' and compPick == 'defense':
                click = False
                print("The Computer chose: ",compPick,"Keep playing")
                messagebox.showinfo("mach",f"The computer chose: {compPick}. Keep playing")
            elif yourChoise == 'defense' and compPick == 'shoot':
                comStack -=1
                click = False
                print("The Computer chose: ",compPick,"Good, you blocked him!!")
                messagebox.showinfo("mach",f"The computer chose: {compPick}. Good, you blocked him!!")
#shoot
            elif yourChoise == 'shoot' and compPick == 'load':
                yourStack -=1
                countWin +=1
                print("The Computer chose: ",compPick,"Good, you shot him!! you win the round (:")
                messagebox.showinfo("mach", f"The computer chose: {compPick}. Good, you shot him!! you win the round (:")
            elif yourChoise == 'shoot' and compPick == 'defense':
                yourStack -=1
                click = False
                print("The Computer chose: ",compPick,"Damm, he blocked you")
                messagebox.showinfo("mach",f"The computer chose: {compPick}. Damm, he blocked you")
            elif yourChoise == 'shoot' and compPick == 'shoot':
                yourStack -=1
                comStack -=1
                click = False
                print("The Computer chose: ",compPick,"STANDOFF!!")
                messagebox.showinfo("mach",f"The computer chose: {compPick}. STANDOFF!!")

        print("your Stack: ", yourStack, "com Stack: ", comStack, "Win: ", countWin, "Lost: ", countLose)

    else:
        if yourChoise == 'load' or yourChoise == 'defense' or yourChoise == 'shoot':
            click = True





label1 = ttk.Label(text = f"your stack: {yourStack}    computer stack: {comStack}    win: {countWin}   lost: {countLose}").pack(side = BOTTOM)
#label1.grid(row = 2, column = 0)

play()
mainloop()
