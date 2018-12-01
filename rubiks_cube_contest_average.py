def list_function():
    my_list = []

    for i in range(5):
        x = float(input("Enter the time for performance " + str(i+1) + ": "))
        my_list.append(x)
        i += 1

    my_list.sort()
    my_list = my_list[1:-1]

    return my_list


def main():
    my_list = list_function()
    index = 0
    total = 0

    while index < len(my_list):
        total += my_list[index]
        index += 1

    average = total / (len(my_list))
    print("The official competition score is " + "{:.2f}".format(average) + " seconds.")

main()