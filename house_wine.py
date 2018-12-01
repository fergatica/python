def main():

    measurements = input("Enter the number of measurements: ")
    measurements = int(measurements)
    counter = 1
    fails = 0
    temp_list = []

    if measurements <= 0:
        print("The number of measurements must be a positive number.")

    else:
        while counter <= measurements:
            temp = input("Enter the temperature " + str(counter) + ": ")
            temp = int(temp)
            temp_list.append(temp)
            int(counter)
            counter += 1

            if counter > 2 and (temp_list[-1] < 20 or temp_list[-1] > 25) \
                    and (temp_list[-2] < 20 or temp_list[-2] > 25):
                print("Your wine is ruined.")
                break

            if temp < 20 or temp > 25:
                fails += 1

            if fails > measurements * 0.1:
                print("Your wine is ruined.")
                break

        if counter > measurements:
            print("Your wine is ready.")


main()

