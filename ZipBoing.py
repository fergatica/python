number = input("How many numbers would you like to have? ")
number = int(number)

count = 1

while count <= number:

    if count % 3 == 0 and count % 7 == 0:
        print("zip boing")
    elif count % 3 == 0:
        print("zip")
    elif count % 7 == 0:
        print("boing")
    else:
        print(count)

    count += 1
