
def read_message():
    """Make the loop for leave a blank input"""
    message_list = []
    while True:
        text_line = input()

        if text_line == "":
            break
        message_list.append(text_line)
    return message_list

def main():
    filename = input("Enter the name of the file: ")
    try:
        save_file = open(filename, mode="w")

    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return
    print("Enter rows of text. Quit by entering an empty row.")
    message = read_message()
    counter = 0
    for lines in message:
        counter += 1
        print(counter, lines, file=save_file)

    save_file.close()

    print(f"File {filename} has been written.")

if __name__ == "__main__":
    main()