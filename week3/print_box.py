"""
Edited and written by Johnson Apanishile
COMP.CS.100 Programming 1
Template for task: box printing
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



def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
