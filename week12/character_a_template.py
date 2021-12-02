"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""
# TODO: the class implementation goes here.
class Character:

    def __init__(self,char_name):
        self.name = char_name
        #creating class variables so they can store methods value swhich are needed
        self.itemlist = []
        self.items = ""
        self.has = ""


    def printout(self):
        print(f"Name: {self.name}")

        unique_list = []

        if self.itemlist==[]:
            print("  --nothing--")

        else:
            for stuffs in self.itemlist:
                if stuffs not in unique_list:
                    unique_list.append(stuffs)

            for unique_stuff in sorted(unique_list):
                if unique_stuff in self.itemlist:
                    count1 = self.itemlist.count(unique_stuff)
                    print(f"  {count1} {unique_stuff}")



    def get_name(self):
        """
        prints out all the given items form the list
        """

        """unique_list = []
                for stuffs in self.itemlist:
                    if stuffs not in unique_list:
                        unique_list.append(stuffs)
                for unique_stuff in unique_list:
                     return unique_stuff"""

        return self.name




    def give_item(self,items):

        self.itemlist.append(items)



    def remove_item(self,item):
        self.itemlist.remove(item)


    def has_item(self,item):
        """
        this method is a comparism between the office item list and a comparism which
        will be proóvides as a parameter and the return value will be true or false (bool)
        this check if the item contents the given item
        passed as a parameter and returns a boolean value
        """

        if item in self.itemlist:
            return True
        else:
                return False


    def how_many(self, item):
        """
        this gets the number of items in the list
        it should count how many times the given
        parameter is seen in the list and return the figure
        """
        num = self.itemlist.count(item)
        return num



def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    #test
    #character3 = Character("Johnson_the beast")


    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()
    #character3.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
