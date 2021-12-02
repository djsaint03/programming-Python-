"""
this was written by Johnson Apanishile
"""
def main():
    num = int(input("How many numbers would you like to have? "))

    for x in range(1, num+1):

        if x % 3 == 0 and x % 7 == 0:
            print("zip boing")

        elif x % 3 == 0:
            print("zip")

        elif x % 7 == 0:
            print("boing")

        else:
            print(x)



if __name__ == "__main__":
    main()