"""
this was written by Johnosn Apanishile
"""

def main():

    Vowels= ['a','e','i','o','u','y']
    word= input("Enter a word: ")
    word_break=list(word)
    vowel_counter = 0
    conso_counter = 0


    for checker in word_break:
        if checker in Vowels:
            vowel_counter +=1
        else:
            conso_counter +=1

    print(f"The word \"{word}\" contains {vowel_counter} vowels and {conso_counter} consonants.", end="")


if __name__ == "__main__":
    main()