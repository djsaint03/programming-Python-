"""
This was written by Johnson Apanishile.
it makes use of conditions to print pre-expected outcomes
"""
def main():
    answer = input("Bored? (y/n) ")
    while answer == "n":
        answer = input("Bored? (y/n) ")

    print("Well, let's stop this, then.")

    result= input("Answer Y or N: ")
    while result != "y" or "n":
        print("Incorrect entry.")

    print("You answered n")
if __name__ == "__main__":
    main()


