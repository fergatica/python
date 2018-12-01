def print_box(a, b, c):
    for i in range(b):
        print(c * a)


def read_input(name):

    user_input = 0

    while user_input <= 0:
        user_input = input(name)
        user_input = int(user_input)

    return user_input


def main():

    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)


main()

