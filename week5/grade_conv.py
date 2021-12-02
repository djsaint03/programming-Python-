"""
this was written and edited by Johnson Apanishile
COMP.CS.100 Programming 1
Code template for "replacing grades" program
"""

# TODO: add the definition for convert_grades here
def convert_grades(grades):
    """
    this function converts the grades higher than 0 to 6
    """
    for scores in range(len(grades)):
        if grades[scores] >= 1:
            grades[scores] = 6
        else:
            grades[scores] = 0

#loop stopped at 5 why?
    """for scores in grades:
        if grades[scores] >= 1:
            grades[scores] = 6
        else:
            grades[scores]=0
    """

def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
