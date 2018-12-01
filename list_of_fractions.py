class Fraction:
    """ This class represents one single fraction that consists of
        numerator and denominator """
    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.
        :param numerator: fraction's numerator
        :param denominator: fraction's denominator
        """
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        elif denominator == 0:
            raise ValueError
        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """ Returns a string-presentation of the fraction in the format
        numerator/denominator """
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator),
                                     abs(self.__denominator))

    def simplify(self):
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = int(self.__numerator/gcd)
        self.__denominator = int(self.__denominator/gcd)


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a


def main():
    print("Enter fractions in the format integer/integer.")
    print("One fraction per line. Stop by entering an empty line.")
    frac_list = []

    line = input()

    while line != "":
        frac_list.append(line)
        line = input()


    print("The given fractions in their simplified form:")
    
    for item in frac_list:
        items = item.split("/")
        frac = Fraction(int(items[0]), int(items[1]))
        frac_string = frac.return_string()
        frac.simplify()
        print(frac_string, "=", frac.return_string())


main()