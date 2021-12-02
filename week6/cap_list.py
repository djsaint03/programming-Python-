"""
this is written by Johnson Apanishile
"""


def capitalize_initial_letters(words):
    """
    this function is called to capitalize a giving parameter
    """

    sentence = words
    new= str.title(sentence)
    return new


"""
    for further check
    compound = words.split()

    for word in range(len(compound)):
        compound[word] = compound[word].lower() #all words are small now
        #compound[word] = compound[word].capitalize()
        for x in compound[word]:
              cap=x.capitalize()
        print(cap, end=" ")
    
   
    for word in compound:
        com = word.capitalize()
        return com

    
    compound = words.split()
    print(compound)
    print(compound[0].capitalize())

    for letters in compound:
        small = letters.capitalize()
        print(small)
       
        small=letters.lower()
        split =small.split()
        #print(split[0].upper())
        print(compound)
        """


def main():
    capitalize_initial_letters("drIVING cAR disoo")


if __name__=="__main__":
    main()