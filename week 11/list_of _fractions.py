
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
        """
        created a list which was used as an object
        """

        a_list = []
        print("Enter fractions in the format integer/integer.")
        print("One fraction per line. Stop by entering an empty line.")

        while True:
            frac = input()

            if frac == " " or frac == "":
                print("The given fractions in their simplified form:")
                break


            frac_main = frac.split("/")

            a_list.append(frac_main)

        for x in a_list:
            #split was displaying as a string so i had to convert it to in from the loop

            simp=Fraction(int(x[0]), int(x[1])) #object prepared for simplification
            simp.simplify()

            print(f"{Fraction(int(x[0]),int(x[1])).return_string()} = {simp.return_string()}")












if __name__ == "__main__":
    main()