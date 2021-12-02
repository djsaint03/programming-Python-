"""
COMP.CS.100 Programming 1
Code Template
this was written and edited by Johnson Apanishile
"""

def read_message():
    """
    reads string and stores in a list
    """
    message_list=[]

    while True:
        input_message = input()
        if input_message == "":
            break
        message_list.append(input_message)
    return message_list



def main():
        print("Enter text rows to the message. Quit by entering an empty row." )
        msg = read_message()


        print("The same, shouting:")
        for x in msg:
            shout_m = x.upper()
            print(shout_m)


if __name__ == "__main__":
    main()
