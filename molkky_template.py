"""
TIE-02100 Introduction to programming
Mölkky
"""

# TODO: Implement the class Player here


class Player:

    def __init__(self, name):
        self.__name = name
        self.__points = 0
        self.__counter = 0
        self.__percentage = 0
        self.__yes_counter = 0

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def has_won(self):
        if self.__points == 50:
            return self

    def add_points(self, pts):
        self.__counter += 1
        self.__points += pts
        if self.__points > 50:
            self.__points = 25
            print(f"{self.__name} gets penalty points!")
        if pts > (self.__points/self.__counter):
            print(f"Cheers {self.__name}!")
        if 40 <= self.__points <= 49:
            print(f"{self.__name} needs only {50 - self.__points} points. It's better to avoid knocking down the pins with higher points.")

    def add_average(self, pts):

        if pts > 0:
            self.__yes_counter += 1

        if self.__yes_counter == 0:
            return
        self.__percentage = (self.__yes_counter / self.__counter) * 100

    def get_average(self):
        return (f"{self.__percentage:.1f}")

def main():

    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!
    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:
        if throw % 2 == 0:
            in_turn = player1
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))
        in_turn.add_points(pts)
        in_turn.add_average(pts)
        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p, hit percentage", player1.get_average())
        print(player2.get_name() + ":", player2.get_points(), "p, hit percentage", player2.get_average())
        print("")

        throw += 1

main()

