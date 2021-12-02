# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    days = int(input("Enter the number of days: "))

    repetition= 1
    zero_count=0
    sum= 0
    avg=0
    while repetition <=days:
        time= float(input(f"Enter day {repetition} running length: "))
        repetition+=1
        sum += time
        avg = float((f"{sum/days:.2}"))

        if days == repetition-1:

            if avg < 3.00:
                print(f"Your running mean of {avg}km was too low!")

            if avg>= 3.00:
                print(f"You were persistent runner! With a mean of {avg} km.")

        if time ==0:
            zero_count+=1
            if zero_count>=3:
                print("lazy lazy")
                break
        else:
            zero_count= 0




if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
