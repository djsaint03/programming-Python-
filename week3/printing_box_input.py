"""
this was written by Johnson Apanishile
COMP.CS.100 Programming 1
Print a box with input error checking
"""
def print_box(w,h,m):
    """
    this function gets the measurement of the object to be created
    :param w:
    :param h:
    :param m:
    :return:
    """
    w=int(w)
    h=int(h)
    for num in range(h):
        print(m*w)

def read_input(value):
    """
    provides condition for print_box function
    :param value:
    :return:
    """
    ans= -1
    while ans <=0:
        ans = int(input(value))
    return ans





def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()

    print_box(width, height, mark)


if __name__ == "__main__":
    main()
