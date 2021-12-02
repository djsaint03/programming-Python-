"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
This was editted by JOhnson Apanishile
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        this method simplifies the numerator and denominor values
        dividing them by the common divisor (calls the greatest_common_divisor function to help)
        and is now used by return_string method
        """
        divisor = greatest_common_divisor(self.__numerator, self.__denominator)

        self.__numerator = int(self.__numerator / divisor)
        self.__denominator = int(self.__denominator / divisor)


#These are the so-called “rich comparison” methods.
# The correspondence between operator symbols and method names is as follows:
# x<y calls x.__lt__(y),
# x<=y calls x.__le__(y),
# x==y calls x.__eq__(y),
# x!=y calls x.__ne__(y),
# x>y calls x.__gt__(y),
# and x>=y calls x.__ge__(y).

    def __lt__(self,obj):
        if self.__numerator/self.__denominator < obj.__numerator / obj.__denominator:
         return True

        else:
            return False

    def __gt__(self, obj):
        if self.__numerator / self.__denominator > obj.__numerator / obj.__denominator:
            return True

        else:
            return False



def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a



def main():
    """
    testing purposes
    """

    frac1 = Fraction(1, 2)
    frac2 = Fraction(2, 3)
    print(frac1 < frac2)
    print(frac1 > frac2)

if __name__ == "__main__":
        main()

