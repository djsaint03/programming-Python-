"""
COMP.CS.100 Programming 1
ROT13 program code template
this is written and edited by Johnson Apanishile
"""

def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    char = text
    char_work = char
    char_work=char_work.lower()

    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    # TODO: implement encryption here


    for i in regular_chars:

        if i == char_work:
            char_index = regular_chars.index(i)
            encrp = encrypted_chars[char_index]
            if char == char.upper():
                final = encrp.upper()

            else:
                final=encrp.lower()
            return final

        else:
            return char_work



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



def main():

   print(encrypt("e"))
   print(row_encryption("Happy, happy, joy, joy!"))


if __name__=="__main__":
    main()