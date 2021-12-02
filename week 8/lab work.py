def main():
    file_name = input("Enter the name of the score file: ")
    dictionary = {}
    try:
        file_save = open(file_name, mode="r")

    except OSError:
        print("There was an error in reading the file.")
        return

    for line in file_save:
        line = line.rstrip()
        try:
            key, value = line.split()
        except ValueError:
            print("There was an erroneous line in the file: ")
            print(line)
            return

        try:
            value = int(value)
        except ValueError:
            print("There was an erroneous score in the file: ")
            print(value)
            return

        if key not in dictionary:
            dictionary[key] = int(value)
        else:
            dictionary[key] += int(value)


    for i in sorted(dictionary):
        print(i, dictionary[i])

if __name__ == "__main__":
    main()
