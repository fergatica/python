import math


def read_input(name):
    user_input = 0

    while user_input <= 0:
        user_input = input(name)
        user_input = float(user_input)

    return user_input


def make_string(a):
    after_string = str("{:.2f}".format(a))
    return after_string


def calc_square_circ(length):
    circumference = length * 4
    print("The total circumference is " + make_string(circumference))


def calc_square_surf(length):
    surface = length * length
    print("The surface area is " + make_string(surface))


def calc_rect_circ(a, b):
    circumference = (a * 2) + (b * 2)
    print("The total circumference is " + make_string(circumference))


def calc_rect_surf(a, b):
    surface = a * b
    print("The surface area is " + make_string(surface))


def calc_circle_circ(a):
    circumference = (a * 2) * math.pi
    print("The total circumference is " + make_string(circumference))


def calc_circle_surf(a):
    surface = (a * a) * math.pi
    print("The surface area is " + make_string(surface))


def menu():

    while True:
        letter = input(
            "Enter the pattern's first letter, q stops this (s/r/q):")
        type(letter)

        if letter == "s":
            square_input = read_input("Enter the length of the square's side: ")
            calc_square_circ(square_input)
            calc_square_surf(square_input)

        elif letter == "r":
            input1 = read_input("Enter the length of the rectangle's side 1:")
            input2 = read_input("Enter the length of the rectangle's side 2:")
            calc_rect_circ(input1, input2)
            calc_rect_surf(input1, input2)

        elif letter == "q":
            return

        else:
            if letter == "c":
                input4 = read_input(
                    "Enter the circle's radius: ")
                calc_circle_circ(input4)
                calc_circle_surf(input4)
            else:
                print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability


def main():
    menu()
    print("Goodbye!")


main()