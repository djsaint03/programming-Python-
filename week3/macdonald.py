"""
this program was edited by Johnson
COMP.CS.100 Programming 1
Template Song: Old MacDonald
"""


def print_verse(name, sound):
    '''
    this function creates each verse of the song
    in the order of each animal and sound
    :param name:
    :param sound:
    :return:
    '''

    if name != 'lamb':
        print(f'''Old MACDONALD had a farm
E-I-E-I-O
And on his farm he had a {name}
E-I-E-I-O
With a {sound} {sound} here
And a {sound} {sound} there
Here a {sound}, there a {sound}
Everywhere a {sound} {sound}
Old MacDonald had a farm
E-I-E-I-O
''')
    else:
        print(f'''Old MACDONALD had a farm
E-I-E-I-O
And on his farm he had a {name}
E-I-E-I-O
With a {sound} {sound} here
And a {sound} {sound} there
Here a {sound}, there a {sound}
Everywhere a {sound} {sound}
Old MacDonald had a farm
E-I-E-I-O''')

def main():
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()

