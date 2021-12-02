"""
This was written by Johnson Apanishile
"""

def main():
        bus_schedule = [630, 1015, 1415, 1620, 1720, 2000]
        count = 0
        projected_times= 3
        search = int(input("Enter the time (as an integer): "))
        while count < len(bus_schedule):
            if search <= bus_schedule[count]:
                break
            count += 1
            if count >= len(bus_schedule):
                count = 0
                break
        print("The next buses leave:")
        for slots in range(count, count + projected_times):
            print(bus_schedule[slots % len(bus_schedule)])


if __name__=="__main__":
    main()