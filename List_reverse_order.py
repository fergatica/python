def list_function():
    my_list = []

    for i in range(5):
        x = int(input("Next number: "))
        my_list.append(x)
        i += 1

    return my_list


def main():
    print("Give 5 numbers:")
    my_list = list_function()

    print("The numbers you entered, in reverse order:")
    index = 0
    size = len(my_list) - 1

    while index <= size:
        print(my_list[size])
        size -= 1

main()