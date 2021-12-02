"""
this was written by Johnson Apanishile
"""

def main():

    num = int(input("How many Fibonacci numbers do you want? "))
    a = 0
    b= 1
    for x in range(1,num+1):
        print(f"{x}. {b}")
        a,b =b,a+b

if __name__ == "__main__":
    main()




