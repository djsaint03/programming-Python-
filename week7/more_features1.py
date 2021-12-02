"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
this was written by Johnson Apanishile
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    # english_spanish= {v:k for k,v in english_spanish.items()}
    convert = list(english_spanish.items())
    convert.sort()
    english_spanish = dict(convert)

    print("Dictionary contents:")

    # sorting using items and lambda function
    sorting_value = sorted(english_spanish.items(), key=lambda k: k[0])

    # using join and a loop to print them in a straight line
    # its looping both keys and values so f"{select the one you want printed out here}"
    print(", ".join(f"{keys}" for keys, value in sorting_value))

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")

            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            new_eng = input("Give the word to be added in English: ")
            new_span = input("Give the word to be added in Spanish: ")

            if new_eng and new_span != " ":
                english_spanish[new_eng] = new_span

            print("Dictionary contents:")

            #sorting using items and lambda function
            sorting_value = sorted(english_spanish.items(), key = lambda k:k[0])

            #using join and a loop to print them in a straight line
            #its looping both keys and values so f"{select the one you want printed out here}"
            print(", ".join(f"{keys}" for keys, value in sorting_value))



        elif command == "R":

            del_word = input("Give the word to be removed: ")
            if del_word not in english_spanish:
                print(f"The word {del_word} could not be found from the dictionary.")
            else:
                english_spanish.pop(del_word)

        elif command == "P":
            # ascending order , converting to list ,sorting and back to list
            convert = list(english_spanish.items())
            convert.sort()
            english_spanish = dict(convert)

            for x in english_spanish:
                print(x, english_spanish[x], end="\n")

        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")

            # joining the dict word found with the string
            phrase = " ".join([english_spanish.get(w, w) for w in sentence.split()])
            print(f"The text, translated by the dictionary: \n{phrase}")


        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
