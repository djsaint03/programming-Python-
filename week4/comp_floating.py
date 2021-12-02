"""
Programming 1 Course
This program was written by Johnson Apanishile

"""


def compare_floats(float1, float2, EPSILON):
    """
    This function compares the absolute float values with
    the Error tolerance EPSILON and returns a true or flase value
    :param float1:
    :param float2:
    :param EPSILON:
    :return:
    """

    if abs(float1-float2)< EPSILON:
        return True
    else:
        return False




def main():

    float1 = float(input("Give an float input"))
    float2 = float(input("Give another float input"))

    print(compare_floats(float1,float2,EPSILON=0.000000001))









if __name__ == "__main__":
    main()