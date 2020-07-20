# משחק תמיד בלולאה אחת!! הם לא עוברים בכמה לולאות
# זכריה ודובי עזרו לי בסידור ובניית המשחק והעיצוב שלו כדי שיעבוד נכון

#Defend Shoot Load game

# building the computer

import random

moves = ["defend", "shoot", "load"]
buletless_move = ["defend", "load"]

keep_playing = True


countBc = 0 # bullets computer
countBp = 0 # bullets player
countWin = 0
countLose = 0

while keep_playing:

    if countBc > 0:
        cmove = random.choice(moves)
    else:
        cmove = random.choice(buletless_move)
 # if you donwt have bullets or wrong word
    pmoves = input("what is your move: defend, load or shoot ?")
    while pmoves != "shoot" and pmoves != "load" and pmoves != "defend":
        pmoves = input("typo: what is your move: defend, load or shoot ?")
    while countBp == 0 and pmoves == "shoot":
        pmoves = input("input agian, you are out of bullets. or defend or load?")

    print("The computer chose", cmove)

# load your stack
    if pmoves == "load":
        countBp +=1
    if cmove == "load":
        countBc +=1

    if pmoves == "shoot" and cmove == "load":
        countBp -=1
        countWin +=1
        print("You win!!")

    elif pmoves == "load" and cmove == "shoot":
        countBc -=1
        countLose +=1
        print("You lose ):")

        # defence and protect
    elif pmoves == "defend" and cmove == "shoot":
        print("good you blocked him")
        countBc -=1

    elif pmoves == "shoot" and cmove == "defend":
        print("Damm, lets try again!")
        countBp -=1

    elif pmoves == "shoot" and cmove == "shoot":
        print("STANDOFF!")
        countBp-=1
        countBc-=1

    print("bullets p: ", countBp, "bullets c: ", countBc)

    if countWin == 3:
        print("YOU WIN THE GAME!!")
        break
    elif countLose == 3:
        print("GAME OVER ):")
        break