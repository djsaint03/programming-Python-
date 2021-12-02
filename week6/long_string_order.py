"""
this was written and editted by johnson apanishile
"""

def longest_substring_in_order(string):
    """
    count longest_substring_in_order
    :param string: count
    :return:
    """
    longest = ""
    max = ""

    for i in range(len(string) - 1):
        if (string[i] <= string[i + 1]):

            longest = longest + string[i]
            if (i == len(string) - 2):
                longest = longest + string[i + 1]

        else:
            longest = longest + string[i]

            if (len(longest) > len(max)):
                max = longest
            longest = ""


    if (len(string) == 1):
        longest = string

    if (len(longest) > len(max)):

        return longest
    else:
        return max

def main():
    pass

if __name__=="__main__":
    main()