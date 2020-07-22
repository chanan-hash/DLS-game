# Defend, Load, Shoot Game

## Description
This is a version of a game wew used to play as kids, one against the other, sometimes also 3 players (a "tripple duel").

## Table of Contents
1. [The rules](#the-rules)
2. [Ongoing round](#ongoing-round)
3. [Game finnish](#game-finnish)
4. [Python game](#python-game)

### The rules:
* Usually it goes as best of 5 rounds, but you can do more or less rounds.
* Each time a new round starts, both players have 0 bullets.
* A round is finnished when 1 player shoot the other, while the other player loads a bullet (therefor he's exposed to being hot at).

### Ongoing roung:
* Remember, a new round starts with 0 bullets for both players.
* In each move, both sides need to choose Either to Load, Shoot, or Defend (both player are choosing the same time)
* If you chose Load, then you get an additional bullet, but you risk at being exposed to being hit by your opponent (if he choose to shoot).
* If you shoot, you have a chance of hitting your opponent, unless he also chooses to shoot, or defend.  
Either way, if you shoot, you waste 1 bullet, so be smart at it.  
(You can't shoot with 0 bullets! If you try to do so - you're just wasting you're turn).
* If you defend, and the opponent shoots you, then you're safe and nothing happens to you (and the opponent wastes 1 bullet).
* The round is finnished when a player shoots while the other loads a bullet (and is exposed).  
(Or if both sides shoot, but only 1 side have bullets).

### Game finnish:
* The game finnishes when the first player wins 3 rounds  
(or more rounds if you choose to extend the game).

# Python game:
* Need python >= 3.6 installed.
* Currently the game is a very simple 1 python file, where you play against the computer, and the computer choose randomly.  
(except for when both player are out of bullets, then you know that no one will shoot, so he'll choose to load, just like you and everyone else would).
* The game is running as a "best of 5" method.

To start the game, all you have to do is this:
```bash
python DLS.py
```
You can try also the other file:
```bash
python dls_dovi.py
```

### The end. Enjoy :-)
