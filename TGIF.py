def main():

    counter = 0;

    for i in range(1, 13):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:  # months that have 31 days
            for j in range(1, 32):
                counter += 1
                if counter % 7 == 3 or counter == 3:
                    print(str(j) + "." + str(i) + ".")

        elif i == 2:
            for j in range(1, 29):
                counter += 1
                if counter % 7 == 3 or counter == 3:
                    print(str(j) + "." + str(i) + ".")

        else:
            for j in range(1, 31):
                counter += 1
                if counter % 7 == 3 or counter == 3:
                    print(str(j) + "." + str(i) + ".")


main()