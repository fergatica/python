# Introduction to Programming
# Named parameters


def print_box(width=0, height=0, border_mark="#", inner_mark=" "):
    upper_part = width * border_mark
    print(upper_part)

    for i in range(height - 2):
        print(border_mark + inner_mark * (width - 2) + border_mark)

    print(upper_part)
    print()


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


main()
