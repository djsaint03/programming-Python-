
def repeat_name(bear_name, repeat):
    for i in range(repeat):
        print(f"{repeat}")

        print(bear_name)


def verse(verse, bear_name):
    print(verse)
    print(bear_name + ",", bear_name, "Bear")
    print(verse)
    print(f"{repeat_name(bear_name, 3)} Bear")
    print(verse)
    print(bear_name + ",", bear_name, "Bear")
    print()


def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


