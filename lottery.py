import math


def probability_calculator(total_balls, drawn_balls):
    after_factorial = math.factorial(total_balls) / (math.factorial(total_balls - drawn_balls) * math.factorial(drawn_balls))
    after_factorial = str("{:.0f}".format(after_factorial))
    print("The probability of guessing all " + str(drawn_balls) +
          " balls correctly is 1/" + after_factorial)


def read_input(total_balls, drawn_balls):
    if total_balls > 0 and drawn_balls <= total_balls:
        probability_calculator(total_balls, drawn_balls)
    elif total_balls <= 0:
        print("The number of balls must be a positive number.")
    elif drawn_balls > total_balls:
        print("At most the total number of balls can be drawn.")


def main():

    total_balls = input("Enter the total number of lottery balls: ")
    total_balls = int(total_balls)
    drawn_balls = input("Enter the number of the drawn balls: ")
    drawn_balls = int(drawn_balls)

    read_input(total_balls, drawn_balls)

main()
