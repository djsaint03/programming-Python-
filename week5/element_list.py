"""
this was written by Johnosn Apanishile
"""

def main():

    num_list=[]
    print("Give 5 numbers: ")
    for x in range(5):
        num = int(input("Next number: "))
        num_list.append(num)
    print(f"The numbers you entered that were greater than zero were: ", end="\n")
    for x in num_list:
        if x >=1:
            print(x)






if __name__== "__main__":
    main()