"""
this was written by Johnson Apanishile
"""

def are_all_members_same(contain):
    """
    this function checks if the provided list
    all contain the same elements
    parameter should be a list
    """
    #for num in contain:
    #if contain.count(contain[0])== len(contain):
        #return print(contain.count(contain[0])is len(contain))
    #else:
        #return print(contain.count(contain[0]) is len(contain))

        # for num in contain:
    #if contain.count(contain[0]) == len(contain):
        #return print(bool(True))
    #else:
        #return print(bool(False))

    """if contain.count(contain[0]) == len(contain):
        return True

    else:
        return False
    """
    return all(x == contain[0] for x in contain)


def main():

    list2 =[44, 44, 44, 44]
    print(are_all_members_same([42, 42, 42, 42, 42]))
    are_all_members_same([44, 44, 44, 44])



if __name__=="__main__":
    main()