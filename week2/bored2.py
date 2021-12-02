"""
This was written by Johnson Apanishile.
"""
def main():
    correct_ansY="Y"
    correct_ansN="N"
    correct_ansy = "y"
    correct_ansn = "n"
    result = input("Answer Y or N: ")
    while result != correct_ansN and result != correct_ansY and result != correct_ansn and result != correct_ansy:
        print("Incorrect entry.")
        result = input("Answer Y or N: ")
    else:
        print("You answered",result)
if __name__ == "__main__":
    main()