# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ristinolla, program code template
def show_grid(list_a):

    for i in range(3):
        for b in range(3):
            if b < 2:
                print(list_a[i][b], end="")
            elif b == 2:
                print(list_a[i][b])
            b += 1
        i += 1


def winner_check(list_a, turns, mark):
    if (list_a[0][0] == list_a[0][1] == list_a[0][2]) and (list_a[0][0] != "." or list_a[0][1] != "." or list_a[0][2] != "."):
        print("The game ended, the winner is " + mark)
        turns = 9
        return turns

    elif (list_a[1][0] == list_a[1][1] == list_a[1][2]) and (list_a[1][0] != "." or list_a[1][1] != "." or list_a[1][2] != "."):
        print("The game ended, the winner is " + mark)
        turns = 9
        return turns

    elif (list_a[2][0] == list_a[2][1] == list_a[2][2]) and (list_a[2][0] != "." or list_a[2][1]!= "." or list_a[2][2] != "."):
        print("The game ended, the winner is " + mark)
        turns = 9
        return turns

    elif (list_a[0][0] == list_a[1][0] == list_a[2][0]) and (list_a[0][0] != "." or list_a[1][0] != "." or list_a[2][0] != "."):
        print("The game ended, the winner is " + mark)
        turns = 9
        return turns

    elif (list_a[0][1] == list_a[1][1] == list_a[2][1]) and (list_a[0][1] != "." or list_a[1][1] != "." or list_a[2][1] != "."):
        print("The game ended, the winner is " + mark)
        turns = 9
        return turns

    elif (list_a[0][2] == list_a[1][2] == list_a[2][2]) and (list_a[0][2] != "." or list_a[1][2] != "." or list_a[2][2] != "."):
        print("The game ended, the winner is " + mark)
        turns = 9
        return turns

    elif (list_a[0][0] == list_a[1][1] == list_a[2][2]) and (list_a[0][0] != "." or list_a[1][1] != "." or list_a[2][2] != "."):
        print("The game ended, the winner is " + mark)
        turns = 9
        return turns

    elif (list_a[2][0] == list_a[1][1] == list_a[0][2]) and (list_a[2][0] != "." or list_a[1][1] != "." or list_a[0][2] != "."):
        print("The game ended, the winner is " + mark)
        turns = 9
        return turns

    elif turns == 9:
        print("Draw!")
        return turns
    else:
        return turns


def grid(mark, x, y, list_a, turns):
    if list_a[y][x] == ".":
        list_a[y][x] = mark
        for i in range(3):
            for b in range(3):
                if b < 2:
                    print(list_a[i][b], end="")
                elif b == 2:
                    print(list_a[i][b])
                b += 1
        i += 1
        turns += 1
        return turns

    else:
        print("Error: a mark has already been placed on this square.")
        return turns


def main():

    # TODO: implement the datastructure for storing the board
    list_a = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

    turns = 0  # How many turns have been played

    show_grid(list_a)

    # The game continues until the board is full.
    # 9 marks have been placed on the board when the player has been
    # switched 8 times.
    while turns < 9:

        # Change the mark for the player
        if turns % 2 == 0:
            mark = "X"
        else:
            mark = "O"

        coordinates = input("Player " + mark + ", give coordinates: ")




        try:
            x, y = coordinates.split(" ")
            x = int(x)
            y = int(y)
            turns = grid(mark, x, y, list_a, turns)
            turns = winner_check(list_a, turns, mark)
                        # TODO: implement the turn of one player here

        except ValueError:
            print("Error: enter two integers, separated with spaces.")

        except IndexError:
            print("Error: coordinates must be between 0 and 2.")



main()
