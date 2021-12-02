"""
This was written by Johnson Apanishile.
this is a multiplication table
"""

def main():
    counter = 0
    max = 10
    sum= 1
    num = int(input("Choose a number: "))
    while counter < max:
        prod = sum*num
        print(f"{sum} * {num} = {prod}")

        counter+=1
        sum+=1




if __name__ == "__main__":
        main()