"""
This is written by Johnson Apanishile
"""



def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    text_input= "I'm on a high way to hell I'm on a high way to hell It's going really well Well it's only hell"
    text=text_input.lower()
    #text = input()

    my_dict = {}

    in_split = text.split()

    #print(in_split)
    #check to make word in list unique
    unique=", ".join(sorted(set(in_split), key=in_split.index))

    print(unique)
    print(in_split)

    #spliting unique list
    split_unique= unique.split()
    #print(split_unique)


    dict.update()


    for xo in in_split:
        checker = in_split.count(xo)
        print(checker, end= ",   ")



"""
    for x in split_unique:
        #count which occurance of word in list
        amount=in_split.count(x)
        if x in in_split:
            new_count = in_split.count(x)
            #print(new_count)

"""
    

        #print(amount, end= ", ")
    #print(in_split.count("hell"))










if __name__ == "__main__":
    main()