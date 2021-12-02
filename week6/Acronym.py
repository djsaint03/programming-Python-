"""
This was written by Johnson Apanishile
"""

def create_an_acronym(wordss):
    """
    this function creates an acronym
    of the string presented in the parameter
    """
    sentence = wordss
    new = str.title(sentence)
    list=new.split()
    store = ""

    for i in list:
        store = store+str(i[0])
    return store



def main():
    print(create_an_acronym("johnson baby powder"))



if __name__=="__main__":
    main()