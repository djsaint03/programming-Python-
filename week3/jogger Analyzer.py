"""
this project was done by Johnson Apanishile
"""

def main():
    days = int(input("Enter the number of days: "))

    day_count = 1
    zero_count = 0
    value = 0
    avg = 0
    count =0

    for x in range(days):
        time = float(input(f"Enter day {day_count} running length: "))
        if time == float(0):
            zero_count += 1
            if zero_count >= 3:
                print("\nYou had too many consecutive lazy days!")
                break
        else:
            zero_count=0

        day_count += 1
        value += time
        avg = round(value / days, 2)
        count +=1
        if count == days:
            if avg < 3.00:
                print(f"\nYour running mean of {avg:.2f} km was too low!")

            if avg >= 3.00:
                print(f"\nYou were persistent runner! With a mean of {avg:.2f} km.")


if __name__ == "__main__":
    main()