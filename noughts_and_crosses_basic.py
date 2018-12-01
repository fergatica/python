# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ristinolla, program code template

def grid(x, y):


    row= "-" * 31
    print(row)
    for i in range(9):
        if i % 3 == 1:
            print("|" + "    " + "." + "    "+ "|" + "    " + "." + "    "+ "|"  + "    " + "." + "    "+ "|")
        else:
            print("|" + "    " + " " + "    "+ "|" + "    " + " " + "    "+ "|"  + "    " + " " + "    "+ "|")

    print(row)


def main():
    grid(0, 0)
    # TODO: implement the datastructure for storing the board
    
    turns = 0  # How many turns have been played

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
        turns += 1

        try:
            x, y = coordinates.split(" ")
            x = int(x)
            y = int(y)

            # TODO: implement the turn of one player here

        except ValueError:
            print("Error: enter two integers, separated with spaces.")

        except IndexError:
            print("Error: coordinates must be between 0 and 2.")


main()
