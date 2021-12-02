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
        divisor = greatest_common_divisor(self.__numerator,self.__denominator)

        self.__numerator = int(self.__numerator/divisor)
        self.__denominator = int(self.__denominator/divisor)

    #Todo: addition for part two

    def complement(self):
        """
        makes either denom or numeron abs and creates a new object as a return value
        """

        """if self.__numerator < 0 or self.__denominator < 0:
            tom = Fraction(abs(self.__numerator), abs(self.__denominator))
            return tom"""

        if self.__numerator <0 or self.__denominator <0:
             return Fraction(abs(self.__numerator),abs(self.__denominator))

        elif self.__numerator >0 or self.__denominator >0:
            return Fraction(-abs(self.__numerator), self.__denominator)

        #else:
               #return Fraction(self.__numerator, self.__denominator)

    def reciprocal(self):
        while True:
            self.__numerator,self.__denominator =self.__denominator, self.__numerator
            return Fraction(self.__numerator, self.__denominator)

    def multiply(self,obj):
        """
        this will take an onject as parameter and multiply it with the
        main object
        """
        numerator = self.__numerator * obj.__numerator
        denominator = self.__denominator * obj.__denominator

        return Fraction(numerator,denominator)


    def divide(self,obj):

        quot1 =  self.__numerator * obj.__denominator
        quot2 = self.__denominator * obj.__numerator

        return Fraction(quot1,quot2)

    def add(self, obj):
        top= (self.__numerator * obj.__denominator) + (obj.__numerator * self.__denominator)
        buttom = self.__denominator * obj.__denominator

        New_sum_obj = Fraction(top, buttom)
        return New_sum_obj


    def deduct(self,obj):
        top = self.__numerator + obj.__numerator
        buttom = self.__denominator * obj.__denominator

        New_dud_obj = Fraction(top, buttom)
        return New_dud_obj





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
    frac = Fraction(2, 4)
    print(frac.return_string())

    complement = frac.complement()
    print(complement.return_string())

    reciprocal = frac.reciprocal()
    print(reciprocal.return_string())

    print("-----------------------------------------")
    frac1 = Fraction(2, 3)
    frac2 = Fraction(4, 5)
    product = frac1.multiply(frac2)
    print(product.return_string())

    print("-----------------------------------------")
    frac1 = Fraction(4, 8)
    frac2 = Fraction(2, 1)
    quotient = frac1.divide(frac2)
    print(quotient.return_string())
    quotient.simplify()
    print(quotient.return_string())

    print("-----------------------------------------")
    frac1 = Fraction(2, 3)
    frac2 = Fraction(1, 6)
    add = frac1.add(frac2)
    print(add.return_string())
    add.simplify()
    print(add.return_string())




if __name__ == "__main__":
    main()
