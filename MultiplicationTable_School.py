def main():
    number = input("Choose a number: ")
    number = int(number)

    count = 1

    while count <= 10:
        total = count * number
        print(count, "*", number, "=", total)
        count += 1


main()