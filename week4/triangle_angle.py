"""
This program was written by Johnson Apansihile
Programming 1 Course
"""


def calculate_angle(angle1,angle2= 90):
    """
    this function calculates and returns the
    third angle of the triangle
    when the two other angles are provided
    """

    angle3 = int(180 - (angle1 + angle2))
    int(angle3)
    return angle3


def main():
    calculate_angle(50, 60)

    calculate_angle(30)


if __name__ == "__main__":
    main()
