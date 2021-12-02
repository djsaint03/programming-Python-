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
            char_index= regular_chars.index(i)
            encrp = encrypted_chars[char_index]
            if char == char.upper():
                final = encrp.upper()

            else:
                final=encrp.lower()
            return final





def row_encryption(sentence):
    """
    this function encrypts a large set of strings
    which calls function encrypt
    """

    combine= ""
    list_of_letters = list(sentence)
    #print(list_of_letters)
    for x in list_of_letters:
        new = x
        en=encrypt(new)
        combine+= en

    return combine



def main():
   print(encrypt("R"))
   print(row_encryption("Happy"))


if __name__=="__main__":
    main()