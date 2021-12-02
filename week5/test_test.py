def input_to_list (number):
    """determine the input numbers"""
    list_number = []
    for i in range (number):
        num=int(input())
        list_number.append(num)
    return list_number


def main():
    round = int(input("How many numbers do you want to process: "))
    print(f"Enter {round} numbers: ")

    name = input_to_list(round)
    searched_number = int(input("Enter the number to be searched: "))
    counting = name.count(searched_number)
    if searched_number in name:
        print(f"{searched_number} shows up {counting} times among the numbers you have entered.")
    else:
        print(f"{searched_number} is not among the numbers you have entered.")

if __name__ == "__main__":
    main()
