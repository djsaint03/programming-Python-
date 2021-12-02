"""
this was written by Johnosn Apanishile
"""

def main():

    num_list=[]
    print("Give 5 numbers: ")
    for x in range(5):
        num = int(input("Next number: "))
        num_list.append(num)
    print("The numbers you entered, in reverse order: ", end="\n")
    for x in reversed(num_list):
        #if x >=1:
            print(x)



if __name__== "__main__":
    main()