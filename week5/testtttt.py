
def main():
    time_table = [630,1015,1415,1620,1720,2000]
    now = int(input("Enter the time (as an integer): "))
    index = 0
    while index < len(time_table):
        if time_table [index] >= now:
            break
        index += 1
        if index >= len(time_table):
            index = 0
            break
        print("The next buses leave:")
        for possible_bus_index in range (index, index + 3):
            print(time_table[possible_bus_index % len(time_table)])



if __name__=="__main__":
    main()