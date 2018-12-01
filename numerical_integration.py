#def parabel(x):
 #   return -pow(x, 2) + 2 * x + 4

def approximate_area(function2, lower, upper, rectangles):

    d = (upper-lower)/rectangles
    i = lower
    summa = 0.0

    while i < upper:
        summa += function2(i)*d

        i += d

    return float(summa)


def main():
    return

main()