#Defend-Load-Shoot game
#Added comment 2

import random

keep_playing = True
playerBullets = 0
botBullets = 0
playerWins = 0
botWins = 0 
botMove = ""
playerMove = ""
nextMoveSentence = "On to the next move"

def nextMove():
    print("player bullets: "+str(playerBullets)+ ", bot bullets: "+str(botBullets))
    print("On to the next move \n")

def gameWon(player):
    global playerBullets, botBullets, playerWins, botWins, keep_playing
    botBullets = 0
    playerBullets = 0
    if player == "bot":
        botWins += 1
    else:
        playerWins += 1
    
    print("The " + player + " wins this round!")
    print("The score is: player - " + str(playerWins) + " , bot - " + str(botWins))
    print("")
    if botWins == 3 or playerWins == 3:
        keep_playing = False


print("Let's start the game!!!")
print("You can always type 'exit' if you wish to stop the game")
print("Good luck :-) \n")

while keep_playing:

    if playerBullets == 0 and botBullets == 0:
        botMove = "load"
    elif botBullets > 0:
        botMove = random.choice(["defend", "load", "shoot"])
    else:
        botMove = random.choice(["defend", "load"])

    playerMove = input("Choose your move - defend, load or shoot: ")
    while playerMove not in ["shoot", "load", "defend", "exit"]:
        playerMove = input("Must choose only: defend, load or shoot! ")
    
    #If human with no bullets, but still choosing with shoot or illiegal move...
    while playerBullets == 0 and playerMove == "shoot" and playerMove not in ["load", "defend", "exit"]:
        playerMove = input("You have no bullets. Must choose only: defend or load! ")
    
    if playerMove == "exit":
        print("The score was: Human - " + str(playerWins) + ", Bot - " + str(botWins) + "\nGood bye. \n")
        exit()
    
    print("The computer chose", botMove)
    
    if playerMove == "load":
        if botMove == "shoot":
            gameWon('bot')
        else:
            playerBullets += 1
            if botMove == "load":
                botBullets += 1
            nextMove()
        
    elif playerMove == "shoot":
        if botMove == "load":
            gameWon('player')
        else:
            playerBullets -= 1
            if botMove == "shoot":
                botBullets -= 1
            nextMove()
    
    else: #if playerMove == "defend"
        if botMove == "shoot":
            botBullets -= 1
        elif botMove == "load":
            botBullets += 1
        nextMove()
    
if playerWins == 3:
    print("And the winner is the human player!!!")
    print("Way to go!! You're the man!! (or woman) ;-) \n")
else:
    print("And the winner is the computer bot!!!")
    print("Sucks for you, human :P \n")
