def main():
    number = input("Choose a number: ")
    number = int(number)

    count = 1
    total = 0

    while total <= 100:
        total = count * number
        print(count, "*", number, "=", total)
        count += 1

main()