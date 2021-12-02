"""
this program was edited by Johnson Apanishile
COMP.CS.100 Programming 1
Code template for the hottest hit song Yogi Bear
"""
def repeat_name(name,repetitions):
    """
    this functions reduces duplicates by
    :param name:
    :param repetitions:
    :return:
    """
    for num in range(repetitions):
        print(f"{name}, {name} Bear")

def verse(song, name ):
    """
    this function prints the verses of the song
    :param song:
    :param name:
    :return:
    """

    if name == "Cindy":
        print(f"{song}\n{name}, {name}")
        print(f"{song}")
        repeat_name(f"{name}", 3)
        print(f"{song}\n{name}, {name} Bear")

    else:
        print(f"{song}\n{name}, {name}")
        print(f"{song}")
        repeat_name(f"{name}", 3)
        print(f"{song}\n{name}, {name} Bear","\n")




def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")



if __name__ == "__main__":
    main()
