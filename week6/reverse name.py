"""
This was written by Johnson Apanishile
"""

def reverse_name(names):
    """
    this function reverses the order of
    name if furfilled by conditions
    """
    list_name = names.split(",")

    if len(list_name) == 1:  # in the text there is no comma
        full_name = list_name[0].strip()
        result = full_name
        return result

    elif list_name[0] == '' or list_name[1] == '':
        list_name.remove('')
        full_name = list_name[0].strip()
        result = full_name
        return result

    elif list_name[0] == ' ' or list_name[1] == ' ':
        list_name.remove(' ')
        full_name = list_name[0].strip()
        result = full_name
        return result


    else:
        full_name = list_name[1].strip() + " " + list_name[0].strip()
        result = full_name
        return result


def main():
    print(reverse_name("Bond,James"))
    print(reverse_name(",James"))
    print(reverse_name("    Bond    ,     James"))
    print(reverse_name("Bond,  "))
    print(reverse_name("Bond James"))
    print(reverse_name(","))
    print(reverse_name("Mando"))




if __name__=="__main__":
    main()