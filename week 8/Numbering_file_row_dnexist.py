"""
This was written by Johnson Apanishile
"""

def main():


    try:
        file_name = input("Enter the name of the file: ")
        file_name = open(file_name,"r")
        counter = 1

        for reader in file_name:
            numbering = reader.strip()
            counter += 1
            print(f"{counter - 1} {numbering}")
        file_name.close()

    except OSError:
      print("There was an error in reading the file.")




if __name__ == "__main__":
    main()