"""
This was written by Johnson Apanishile
COMP.CS.100 Programming 1
Code template for geometric patterns.
"""
from math import pi


def square_area(side):
    """
    calculates the area of a square and requires
    the side as an input
    """
    area = f"{side*side:.2f}"
    return area

def square_cir(side):
    """
        calculates the circumference of a square and requires
        the side as an input
    """
    cir = f"{4*side:.2f}"
    return cir

def rect_cir(length1, length2):
    """
        calculates the acircumference of a rectangle and requires
        the two length parameters
    """
    cir_rec = f"{2*(length1+length2):.2f}"
    return cir_rec


def rect_sa(length1, length2):
    """
        calculates the area of a rectangle and requires
        the two lengths as an input
    """
    sa = f"{length1 * length2:.2f}"
    return sa


def circumference(radius):
    """
        calculates the circumference of a circle and requires
        the radius as an input
    """
    circum = round(2*pi*radius,2)
    return circum


def c_sa(radius):
    """
        calculates the area of a circle and requires
        the radius as an input
    """
    area = round(pi*(radius**2),2)
    return area




def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            # Replace this comment and "pass" with your function calls dealing
            # with square.
            side = float(input("Enter the length of the square's side: "))

            while side <=0.0:
                side = float(input("Enter the length of the square's side: "))
                if side >=0.0:
                    break

            print(f"The circumference is {square_cir(side)}")
            print(f"The surface area is {square_area(side)}")
            print()



        elif answer == "r":
            # Replace this comment and "pass" with your function calls dealing
            # with rectangle.
            side1= float(input("Enter the length of the rectangle's side 1: "))
            #side2 = float(input("Enter the length of the rectangle's side 2: "))

            while side1 <=0.0:
                side1 = float(input("Enter the length of the rectangle's side 1: "))

            side2 = float(input("Enter the length of the rectangle's side 2: "))
            while side2 <=0.0:
                side2 = float(input("Enter the length of the rectangle's side 2: "))

            print(f"The circumference is {rect_cir(side1, side2)}")
            print(f"The surface area is {rect_sa(side1, side2)}")
            print()


        elif answer == "c":
            radius= float(input("Enter the circle's radius: "))

            print(f"The circumference is {circumference(radius)}")
            print(f"The surface area is {c_sa(radius)}")
            print()


        elif answer == "q":
            return  print("Goodbye!")


        else:
            print("Incorrect entry, try again!")
            print()


        # Empty row for the sake of readability.
        #print()

def main():
    menu()
    #print("Goodbye!")

if __name__ == "__main__":
    main()
