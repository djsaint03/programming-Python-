"""
This program was written by Johnson Apanishile
Programming 1 course

"""

def main():

    number = int(100)

    for num in range(0,number+1,2):
        print(num)
    for rev in range(number,-1,-2):
        print(rev)


if __name__ == "__main__":
    main()