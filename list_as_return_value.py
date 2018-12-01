def input_to_list(a):
    my_list = []
    print("Enter " + str(a) + " numbers:")
    a = int(a)
    for i in range(a):
        x = int(input())
        my_list.append(x)
        i += 1

    return my_list

def main():

    user = int(input("How many numbers do you want to process: "))
    my_list = input_to_list(user)
    search = int(input("Enter the number to be searched: "))
    repetitions = 0
    index = 0
    size = len(my_list) - 1

    while index <= size:
        if my_list[index] == search:
            repetitions += 1
        index += 1

    if repetitions > 0:
        print(str(search) + " shows up " + str(repetitions) +
              " times among the numbers you have entered.")
    else:
        print(str(search) + " is not among the numbers you have entered.")



main()