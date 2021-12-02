"""
This was written by Johnson Apanishile
programming 1 courses

"""


def print_box(w,h,m):
    """
    this function gets the measurement of the object to be created
    :param w:
    :param h:
    :param m:

    """
    w=int(w)
    h=int(h)
    for num in range(h):
        print(m*w)


def read_input(inputs):
    """
    this function gets the measurement of the object to be created
    :param inputs:
    :return inputs:
    """

    if inputs == "Enter the width of a frame: ":
        while True:
            try:
                inputs = int(inputs)
                break
            except ValueError:
                inputs = input("Enter the width of a frame: ")


    if inputs == "Enter the height of a frame: ":
        while True:
            try:
                inputs = int(inputs)
                break
            except ValueError:
                inputs = input("Enter the height of a frame: ")
    return inputs



def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()