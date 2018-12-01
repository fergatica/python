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

    def complement(self):
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""

        complement = abs(self.__denominator) - abs(self.__numerator)

        return "{:s}{:d}/{:d}".format(sign, complement,
                                      abs(self.__denominator))

    def reciprocal(self):
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""

        return "{:s}{:d}/{:d}".format(sign, abs(self.__denominator),
                                      abs(self.__numerator))

    def multiply(self, other):
        top = self.__numerator * other.__numerator
        bottom = self.__denominator * other.__denominator

        return "{:d}/{:d}".format(top, bottom)

    def divide(self, other):
        top = self.__numerator * other.__denominator
        bottom = self.__denominator * other.__numerator

        return "{:d}/{:d}".format(top, bottom)

    def add(self, other):
        new_denom = self.__denominator * other.__denominator
        new_numer = (self.__numerator * other.__denominator) + (
                    other.__numerator * self.__denominator)
        return "{:d}/{:d}".format(new_numer, new_denom)


    def deduct(self, other):
        new_denom = self.__denominator * other.__denominator
        new_numer = (self.__numerator * other.__denominator) - (
                    other.__numerator * self.__denominator)
        return "{:d}/{:d}".format(new_numer, new_denom)


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a



def main():
    frac1 = Fraction(2, 3)
    frac2 = Fraction(1, 6)

    print(frac1.add(frac2))

    frac3 = Fraction(4, 8)
    frac4 = Fraction(2, 1)

    print(frac3.divide(frac4))

main()
