

def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    # TODO: implement encryption here

    enter_text = ""
    if text.isupper():
        lower = text.lower()
        if lower in regular_chars:
            for index in range(0, len(regular_chars)):
                if lower == regular_chars[index]:
                    enter_text = (encrypted_chars[index]).upper()
        else:
            enter_text = lower
    else:
        if text in regular_chars:
            for index in range(0, len(regular_chars)):
                if text == regular_chars[index]:
                    enter_text = encrypted_chars[index]
        else:
            enter_text = text
    return enter_text


def row_encryption(sentence):
    """
    this functions takes strings as parameters
    and encrypts a larger string set
    """
    combine = ""
    for letters in sentence:
        # Convert to number with ord.
        convert = ord(letters)

        # Shift number back or forward.
        if convert >= ord('a') and convert <= ord('z'):
            if convert > ord('m'):
                convert -= 13
            else:
                convert += 13
        elif convert >= ord('A') and convert <= ord('Z'):
            if convert > ord('M'):
                convert-= 13
            else:
                convert += 13
        # Append to result.
        combine += chr(convert)

    # Return transformation.
    return combine


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