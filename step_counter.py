"""
Code Name: Step Counter
Email: pino.gatica.fernanda.x@uta.fi
Student Number: 284791
Name: Fernanda Pino

Program Goal: The program asks for the amount of steps/day, one day per line.
and ends by entering an empty row. It later checks how many days there was
under 1000 steps and removes this and reports it to the user unless no steps
are removed.
If there are any days left with steps over 1000 it
It then calculates the amount of days steps ranged from:
    1000-4999, 5000-8999, 9000-12999, and so on (adding 4k at a time)
    and displays them to the user in a graphical manner
Then it tells the user the step amount it had most days and informs this
It also calculates the days with over 9k steps and the longest distance the
user walked in one day as well as total month calorie consumption
"""


def steps_per_day():
    """
    This function takes input from the user and appends it to a list
    if the input is an empty string aka "enter" it will quit the function

    :return: list of days the user has input
    """
    days_list = []
    while True:
        user_input = input()
        if user_input == "":
            break
        days_list.append(user_input)

    return days_list


def list_of_string_to_int(days_list):
    """
    function converts the user input from string to int to be able to perform
    math expressions

    :param days_list: list of steps/day from the user
    :return: new list in the int format
    """

    days_list = [int(i) for i in days_list]
    return days_list


def numbers_over_1k(days_list):
    """
    this function creates a new list which includes only the numbers over
    1000 steps from the list used as parameter

    :param days_list: days input by the users (in int format)
    :return: new list of days, only if over 1k steps a day
    """
    counter = 0
    new_list = []

    for i in days_list:

        if i >= 1000:
            new_list.append(i)
        counter += 1

    return new_list


def longest_distance_walked(days_list_over1k):
    """
    function finds the highest amount of steps walked within one day from
    the data set. It then converts this to km

    :param days_list_over1k: gets list of days over 1k
    :return: longest distance walked in one day (km format)
    """
    longest_distance = 0

    # finds longest distance
    for i in days_list_over1k:
        if i > longest_distance:
            longest_distance = i

    # expression to find hoy make km is one step
    one_step_in_km = 1.5/2500
    # multiplies the highest amount of steps with the length in km of one step
    longest_distance_km = one_step_in_km * longest_distance

    return longest_distance_km


def total_calories(days_list_over1k):
    """calculates the amount of calories the user consumed with that amount of
    steps over the data set period of time

    :param days_list_over1k: list of steps over 1k walked per day
    :return: total calorie consumption from data set
    """

    total_steps = 0
    steps_per_km = 1.5
    kcal_per_km = 50

    for i in days_list_over1k:
        total_steps += i

    one_step_in_km = steps_per_km / 2500

    total_kcal = total_steps * one_step_in_km * kcal_per_km

    return total_kcal


def graphical_representation(days_list_over1k):
    """function takes the distances and creates categories from 1k and adds
    4k steps every time and creates a dictionary and adds the amount of
    repetitions of days in numerical form. Tt then prints theses in the
    graphical manner of #

    :param days_list_over1k:
    :return: dictionary of categories and values
    """
    longest_distance = 0
    slots_list = []
    # finds longest distance from data set
    for i in days_list_over1k:
        if i > longest_distance:
            longest_distance = i

    # finds how many times you can substract 4k from the longest distance
    # without going under 1k and ignoring the remainder
    slots = (longest_distance - 1000) // 4000
    # identifies the max category from the most steps
    last_slot = slots * 4000 + 1000

    # assigns the amount of slots to a list and organizes it from less to more
    while last_slot >= 1000:
        slots_list.append(last_slot)
        last_slot -= 4000
    slots_list.reverse()

    # creates dictionary and assigns keys from the slot list and add 0 as value
    found_dict = {}
    for slot in slots_list:
        found_dict[slot] = 0

    # iterates over days list and slot list and adds repetition of values
    for item in days_list_over1k:
        for slot in slots_list:
            if item >= slot and item <= (slot+3999):
                found_dict[slot] += 1

    # prints a hashtag for every day within category
    for i in found_dict:
        print(i, end =" ")
        print(found_dict[i]*"#")

    return found_dict


def steps_taken_most_days(found_dict):
    """function finds the highest value amongst keys

    :param found_dict:
    :return: the range of steps repeated most often
    """

    most_days = (max(found_dict, key=found_dict.get))

    return "over " + str(most_days) + " but under " + str(
        most_days+4000) + " steps"


def over_9k_steps(days_list_over1k):
    """
    finds the total amount of days where over 9k were walked

    :param days_list_over1k: list of steps per day
    :return: returns amount of days over 9k steps a day
    """

    days = 0
    for i in days_list_over1k:
        if i >= 9000:
            days += 1

    return days


def main():
    print("Enter the amount of steps/day, one day per line.")
    print("End by entering an empty row.")

    days_list = steps_per_day()     # build a list of steps/day from user input
    days_list = list_of_string_to_int(days_list)    # values from str to int
    amount_of_days = (len(days_list))  # gives length of the list

    if amount_of_days > 0:
        print("Information related to the period of measurement (" + str(
            amount_of_days) + " days):")

    # total amount of days minus total amount of days over 1k
    # give the rejected days
    days_rejected = amount_of_days - len(numbers_over_1k(days_list))

    # prints only if 1 or more days were rejected
    if days_rejected >= 1:
        print("Rejected " + str(
            days_rejected) + " results of under 1000 steps/day. ")
    print()

    # if are any amount of days are not rejected it read the rest of the code
    if amount_of_days - days_rejected >= 1:
        print("Graphical representation of information:")
        days_list_over1k = numbers_over_1k(days_list)
        found_dict = graphical_representation(days_list_over1k)
        print()

        print("Steps taken during most of the days: ", end="")
        print(steps_taken_most_days(found_dict))

        steps_taken_most_days(found_dict)
        print("Days with over 9000 steps taken: ", end="")
        print(over_9k_steps(days_list_over1k), end="")
        print(" days")

        longest_distance = str(
            "{:.2f}".format((longest_distance_walked(days_list_over1k))))
        print("Longest distance walked during a day: " + longest_distance + " km")

        total_kcal = str("{:.0f}".format(total_calories(days_list_over1k)))
        print("Total calories consumed by walking: " + total_kcal + " kcal")


main()