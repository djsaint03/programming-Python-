"""
COMP.CS.100 Programming 1
this is written and edited by Johnson Apanishile
"""

def count_abbas(word):
    """
    function looks for the search varible in the given
    parameter word.
    and return the number of time it counts
    """

    counter = 0
    index = 0
    search = "abba"

    while word == word:
        index = word.find(search, index)
        if index >= 0:
            counter += 1
            index += 1
        else:
            break

    return counter


"""
    #if listword[check]== "a" and listword[check+indi]== "b" and listword[check]== "b" and listword[check]== "a":
            #counter +=1

def count_abbas(name):
    need= list("abba")
    count= 0
    listed = list(name)
    print(need)

    for check in listed:
        if check in need:
            count+=1
            check
            return count

"""
def main():
    print(count_abbas("abbabbabba"))
    print(count_abbas("abbabbabbabbabbabababbaabba"))
    print(count_abbas("abbabba"))



if __name__=="__main__":
    main()