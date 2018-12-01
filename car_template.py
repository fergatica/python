# Fill in all TODOs in this file

import math
# This is a text-based menu. You should ONLY touch TODOs inside the menu.
# TODOs in the menu call functions that you have implemented and take care
# of the return values of the function calls.


def menu():
    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)


        elif choice == "3":
            break

    print("Thank you and bye!")


# This function has three parameters which are all FLOATs:
#       (1) the size of the tank
#       (2) the amount of gas that is requested to be filled in
#       (3) the amount of gas in the tank currently
#
# The parameters have to be in this order.
# The function returns one FLOAT that is the amount of gas in the
# tank AFTER the filling up.
#
# The function does not print anything and does not ask for any
# input.


def fill(tank_size, to_fill, gas):
    if (gas + to_fill) > tank_size:
        gas = tank_size
        return gas
    else:
        gas = gas + to_fill
        return gas

# This function has six parameters. They are all floats.
#   (1) The current x coordinate
#   (2) The current y coordinate
#   (3) The destination x coordinate
#   (4) The destination y coordinate
#   (5) The amount of gas in the tank currently
#   (6) The consumption of gas per 100 km of the car
#
# The parameters have to be in this order.
# The function returns three floats:
#   (1) The amount of gas in the tank AFTER the driving
#   (2) The reached (new) x coordinate
#   (3) The reached (new) y coordinate
#
# The return values have to be in this order.
# The function does not print anything and does not ask for any
# input.


def drive(x, y, new_x, new_y, gas, gas_consumption):
    # It might be useful to make one or two helper functions to help
    # the implementation of this function (drive)
    distance_x = new_x - x
    distance_y = new_y - y
    distance_wanted = distance_wanted_to_drive(distance_x, distance_y)
    distance_possible = possible_distance_to_drive(gas_consumption, gas)

    if distance_wanted <= distance_possible:
        gas = gas - ((gas_consumption/100) * distance_wanted)
        x = new_x
        y = new_y
        return gas, x, y

    elif distance_wanted > distance_possible:
        x, y, gas = out_of_gas_coordinates(distance_possible, distance_wanted, x, y, new_x, new_y)
        return gas, x, y
        #then move only the amount it cas on the hypothenuse


"""TODO"""
# Implement your own functions here. It is required to implement at least
# two functions that take at least one parameter and return at least one
# value.
# The functions have to be used somewhere in the program.


def read_number(prompt, error_message="Incorrect input!"):

    # This function reads input from the user.
    # Do not touch this function.
    try:
        return float(input(prompt))
    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def possible_distance_to_drive(gas_consumption, gas):
    return (100/gas_consumption) * gas


def distance_wanted_to_drive(x, y):
    wanted = math.sqrt((x * x) + (y * y))
    return wanted


def out_of_gas_coordinates(p, m, x, y, new_x, new_y):
    x = x + (p * (new_x - x)) / m
    y = y + (p * (new_y - y)) / m
    gas = 0
    return x, y, gas


def main():
    menu()


main()
