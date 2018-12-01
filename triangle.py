from math import sqrt


def area(first, second, third):
    total = (first + second + third) / 2
    final = sqrt(total*(total-first)*(total-second)*(total-third))
    return final


def main():
    first = input("Enter the length of the first side: ")
    first = float(first)
    second = input("Enter the length of the second side: ")
    second = float(second)
    third = input("Enter the length of the third side: ")
    third = float(third)

    final = area(first, second, third)

    print("The triangle's area is ", end="")
    print("{:.1f}".format(final))


main()

