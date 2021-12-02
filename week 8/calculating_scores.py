"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150421047
Name: Johnson apanishile
Email: johnson.apanishile@tuni.fi

calculating scores given from a file
"""


def main():
    """
    file will be looped in a dictionary and sorted then printed
    """
    file_name = input("Enter the name of the score file: ")
    file = open(file_name, "r")

    dict = {}
    for liners in file:
        #key and value with split seperates your list value
        key,value = liners.split()

        if key in dict:
            #if dict key more than one, add the values
            dict[key]+= int(value)

        else:
            dict[key] = int(value)
    print("Contestant score:")

    #print key and value which is being sorted using sort and items()
    for key,value in sorted(dict.items()):
        print(f"{key} {value}")



if __name__ == "__main__":
    main()