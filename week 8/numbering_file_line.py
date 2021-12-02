"""
Name: Johnson Apanishile
programming course 1

"""

def read_message():
    """
    function reads inputs and breaks if empty line is given 
    """

    list_message= []
    while True:
        text_line = input()

        if text_line == "":
            break
        list_message.append(text_line)
    return list_message

def main():

    file_name = input("Enter the name of the file: ")
    try:
        file = open(file_name,"w")

    except OSError:
        print(f"Writing the file {file_name} was not successful.")
        return
    print("Enter rows of text. Quit by entering an empty row.")
    message = read_message()
    counter = 0

    for reader in message:
        counter += 1
        print(counter, reader, file= file)

    file.close()

    print(f"File {file_name} has been written.")


if __name__ == "__main__":
    main()