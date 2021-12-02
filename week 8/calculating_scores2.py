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
    dict = {}

    try:
        file = open(file_name, "r")

    except OSError:
        print("There was an error in reading the file.")
        return

    for liners in file:
        #key and value with split seperates your list value
        liners= liners.rstrip()
        try:
            key,value = liners.split()
        except ValueError:
            print("There was an erroneous line in the file: ")
            print(liners)
            return

        try:
            value = int(value)
        except ValueError:
            print("There was an erroneous score in the file: ")
            print(value)
            return

        if key not in dict:
            #if dict key more than one, add the values
            dict[key] = int(value)

        else:
            dict[key] += int(value)



    for i in sorted(dict.items()):
        print(i,dict[i])



if __name__ == "__main__":
    main()