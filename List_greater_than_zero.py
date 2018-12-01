def list_function():
    my_list = []

    for i in range(5):
        x = int(input("Next number: "))
        if x > 0:
            my_list.append(x)
        i += 1

    return my_list


def main():
    print("Give 5 numbers:")
    my_list = list_function()
    print("The numbers you entered that were greater than zero were:")
    index = 0

    while index < len(my_list):
        print(my_list[index])
        index += 1

main()