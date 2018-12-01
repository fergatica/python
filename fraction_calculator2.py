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
        top = int(self.__numerator / gcd)
        bottom = int(self.__denominator / gcd)
        return "{:d}/{:d}".format(top, bottom)

    def multiply(self, other):
        top = self.__numerator * other.__numerator
        bottom = self.__denominator * other.__denominator
        return Fraction(top, bottom)


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a


'''def simplify(a, b):
    gcd = greatest_common_divisor(a, b)
    a = int(a/gcd)
    b = int(b/gcd)
    return a, b'''


def main():
    frac_dict = {}
    operations_dict = {'*': "", "/": "", '+': "", "-": ""}


    while True:
        command = input("> ")
        if command == "add":
            value = input("Enter a fraction in the form integer/integer: ")
            name = input("Enter a name: ")
            values = value.split("/")
            frac = Fraction(int(values[0]), int(values[1]))
            frac_dict[name] = frac
        elif command == "quit":
            print("Bye bye!")
            return
        elif command == "print":
            name = input("Enter a name:")
            if name in frac_dict:
                print(name, "=", frac_dict[name].return_string())
            elif name not in frac_dict:
                print(f"Name {name} was not found")
        elif command == "list":
            for item in sorted(frac_dict):
                print(item, "=", frac_dict[item].return_string())


        elif command == "file":
            file_name = input("Enter the name of the file: ")
            file = "closed"
            line = "a"
            try:
                f = open(file_name, "r")
                file = "is_open"
            except FileNotFoundError:
                print("Error: the file cannot be read.")
            if file == "is_open":
                line = f.readline().strip("\n")
                while line != "":
                    line = line.replace("=", "/")
                    values = line.split("/")
                    name = values[0]
                    fraction = Fraction(int(values[1]), int(values[2]))
                    frac_dict[name] = fraction
                    line = f.readline().strip("\n")

        elif command == "*":
            fraction_one = input("1st operand: ")
            if fraction_one not in frac_dict:
                print(f"Name {fraction_one} was not found")

            else:
                fraction_two = input("2nd operand: ")
                if fraction_two not in frac_dict:
                    print(f"Name {fraction_two} was not found")
                else:
                    a = frac_dict[fraction_one]
                    b = frac_dict[fraction_two]
                    result = a.multiply(b)
                    simplified = result.simplify()
                    print(frac_dict[fraction_one].return_string(), "*",
                          frac_dict[fraction_two].return_string(), "=",
                          result.return_string())
                    print("simplified", simplified)

        elif command in operations_dict:
            print("yes!", command)

        else:
            print("Unknown command!")


'''

    for item in frac_list:

        frac = Fraction(int(items[0]), int(items[1]))
        frac_string = frac.return_string()
        frac.simplify()
        print(frac_string, "=", frac.return_string())'''
main()