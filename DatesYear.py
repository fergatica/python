for i in range(1, 13):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        for j in range(1, 32):
            print(str(j) + "." + str(i) + ".")
    elif i == 2:
        for j in range(1, 29):
            print(str(j) + "." + str(i) + ".")
    else:
        for j in range(1, 31):
            print(str(j) + "." + str(i) + ".")


