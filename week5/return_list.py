"""
This was written by Johnson Apanishile
"""
def main():
    list= []

    ask = int(input("How many numbers do you want to process: "))

    print(f"Enter {ask} numbers:")
    for x in range(ask):
        num=int(input())
        list.append(num)


    search = int(input("Enter the number to be searched: "))

    count = list.count(search)
    if search in list:
        print(f"{search} shows up {count} times among the numbers you have entered.")
    else:
        print(f"{search} is not among the numbers you have entered.")



if __name__=="__main__":
    main()