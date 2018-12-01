playerOne = input('Player 1, enter your choice (R/P/S): ')
playerTwo = input('Player 2, enter your choice (R/P/S): ')

if playerOne == playerTwo:
    print("It's a tie!")

elif (playerOne == "P" and playerTwo == "S") or (playerOne == "p" and playerTwo == "s"):
    print("Player 2 won!")

elif playerOne == "P" and playerTwo == "R":
    print("Player 1 won!")

elif playerOne == "S" and playerTwo == "P":
    print("Player 1 won!")

elif playerOne == "S" and playerTwo == "R":
    print("Player 2 won!")

elif playerOne == "R" and playerTwo == "P":
    print("Player 2 won!")

elif playerOne == "R" and playerTwo == "S":
    print("Player 1 won!")