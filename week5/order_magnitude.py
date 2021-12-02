"""
this was written by Johnson Apanishile
"""

def is_the_list_in_order(array):
    """
    this functions verifies if the list is ordered
    and returns bool statements
    """

    new_arr = sorted(array)
    if array == new_arr:
        return True

    else:
        return False

def main():
    print(is_the_list_in_order([37, 42, 43]))
    print(type(is_the_list_in_order([37, 42, 43])))



if __name__=="__main__":
    main()