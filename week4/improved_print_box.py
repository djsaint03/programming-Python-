"""
COMP.CS.100 Programming 1
Assignment "Improved Box Printing" code template
This was edited by Johnson Apanishile
"""

# TODO: the definition of print_box goes here unless it goes after main.
def print_box(width,height,border_mark="#",inner_mark=" "):
    """
    this function gets the measurement of the object to be created
    :param width:
    :param height:
    :param border_mark:
    :return:
    """
    w = int(width)
    h = int(height)
    for x in range(h):
        for y in range(w):
            if (x==0 or x==h-1 or y==0 or y==w-1):
                print(border_mark,end="")
            else:
                print("",end=inner_mark)
        print()
    print()


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()
