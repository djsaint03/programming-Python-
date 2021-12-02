"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
this was editted by Johnson Apanishile
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    # TODO: Define all the methods here.  You can see what they are,
    #       what parameters they take, and what their return value is
    #       by examining the main-function carefully.
    #
    #       You also need to consider which attributes the class needs.
    #
    #       You are allowed to modify the main function, but your
    #       methods have to stay compatible with the original
    #       since the automatic tests assume that.

    def __init__(self, name, price, sale= 0.0):
        """
        constructor method which collects
        name ,price , sale parameters
        """
        self.__name = name
        self.__price = float(price)
        self.__sale = float(sale)


    def set_sale_percentage(self,sale):
        """
        this sets the sales price
        requires sales parameter
        """
        self.__sale= sale


    def get_price(self):
        """
        this method introduces a conditional statement
        which checks if the items has a sales% or not
        if sales %  percent then calculate
        """

        if self.__sale == 0.0:
            return self.__price
        if self.__sale >0:
            return self.__price -(self.__price * (self.__sale/100))

    def printout(self):
        """
        this method prints out price and sales
        """
        print(f"price: {self.__price}")
        print(f"sale%: {self.__sale}")


def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
