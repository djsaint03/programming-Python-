"""
This was edited and written by Johnson Apanishile
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
"""

from math import sqrt


def area(a,b,c):
    """
    this function calculates the area of a triangle
    using parameters which are inputs from the main function and returned
    :param a:
    :param b:
    :param c:
    :return:
    """
    a = float(a)
    b = float(b)
    c = float(c)


    s = float((a + b + c) / 2)
    area_v = float((s * (s - a) * (s - b) * (s - c)) ** 0.5)
    return area_v

def main():
    a = input("Enter the length of the first side: ")
    b = input("Enter the length of the second side: ")
    c = input("Enter the length of the third side: ")

    print("The triangle's area is",round(area(a,b,c),1))


if __name__ == "__main__":
    main()
