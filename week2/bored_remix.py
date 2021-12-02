"""
This was written by Johnson Apanishile.
"""
def main():
    options =["y","Y","N","n"]
    answer = input("Bored? (y/n) ")

    if options[0] == answer:
        print("Well, let's stop this, then.")

    while answer not in options:
        print("Incorrect entry.")
        answer = input("Bored? (y/n) ")




    while "N" or "n"  ==answer:
            answer = input("Bored? (y/n) ")









if __name__ == "__main__":
    main()