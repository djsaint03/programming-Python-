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
    fraction calculator using just the main functions

    """


    obj_dic = { }


    while True:
        display = input("> ")
        if display == "add":
            info = input("Enter a fraction in the form integer/integer: ").split("/")
            if info != "" or info != " ":
                name= input("Enter a name: ")
                obj_dic[name]=info

        elif display =="print":
            search= input("Enter a name: ")
            if search in obj_dic:
                x =obj_dic[search]
                new_val= f"{int(x[0])}/{int(x[1])}"
                print(f"{search} = {new_val}")
            else:
                print(f"Name {search} was not found")

        elif display == "list":
            for k,v in sorted(obj_dic.items()):
                print(f"{k} = {int(v[0])}/{int(v[1])}")

        elif display == "*":
            op1 = input("1st operand: ")
            if op1 not in obj_dic:
                print(f"Name {op1} was not found ")

            else:
                op2 = input("2nd operand: ")

                if op2 in obj_dic:
                    op11 = obj_dic[op1]
                    op22 = obj_dic[op2]

                    print(f"{int(op11[0])}/{int(op11[1])} * {int(op22[0])}/{int(op22[1])} = {int(op11[0])* int(op22[0])}/{int(op11[1])* int(op22[1])}")

                    print(f"simplified {1}/{(int(op11[1])* int(op22[1])) // int(op22[0])}")

                else:
                    print(f"Name {op2} was not found ")

        elif display == "file":
            filename= input("Enter the name of the file: ")
            if filename != "fractions.txt":
                print("Error: the file cannot be read.")

            else:
                f= open(filename, "r")
                lists=f.read()






        elif display == "quit":
            print("Bye bye!")
            break

        else:
            print("Unknown command!")




if __name__ == "__main__":
    main()
