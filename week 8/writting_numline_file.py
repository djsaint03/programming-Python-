"""
Name: Johnson Apanishile
programming course 1

"""

def read_message():
        pass

def main():
        file_name = input("Enter the name of the file: ")

        try:
            file_name = open(file_name, "w")


        except OSError:
            print(f"Writing the file {file_name} was not successful.")
            return

        for lines in file_name:
            text = input("Enter rows of text. Quit by entering an empty row.")
            if lines == "":
                exit()
            else:
                file_name.write(text)

                file_name.close()





if __name__ == "__main__":
    main()