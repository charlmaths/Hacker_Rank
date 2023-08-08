""" Rock paper scissors game - A player puts an input then using random module,
play against the computer
"""

import random


def rpsGame():
    """ Function for choices """
    player = input("Please select: Rock, Paper, or Scissors: ")
    player.lower()
    rpslist = ["rock", "paper", "scissor"]
    computer = random.choice(rpslist)
    choices = {"Player":player, "Computer":computer}
    return choices

# print(rpsGame())

def gameChecker(player, computer):
    """ Method for checking and comparing the choices for player and computer """
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Player wins! Rock beats Scissors"
        else:
            return "Computer wins! Paper beats Rock"
    elif player == "paper":
        if computer == "rock":
            return "Player wins! Paper beats Rock"
        else:
            return "Computer wins! Scissors beats Paper"
    elif player == "scissors":
        if computer == "paper":
            return "Player wins! Scissors beat Paper"
        else:
            return "Computer wins! Rock beats Scissors"

#################### GAME BELOW ######################

print("")
rps_game = rpsGame()
game_results = gameChecker(rps_game["Player"], rps_game["Computer"])
print(game_results)
print("")
