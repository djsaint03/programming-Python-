"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
This program models a character adventuring in a video game.
THis was editted by Apanishile Johnson
"""

class Character:
    """
    This class defines what a character is int he game and what
    he or she can do.
    """

    # TODO: copy your Character class implementation from
    #       the previous assignment here and implement the
    #       following new methods.
    #
    #       Also note, that you have to modify at least
    #       __init__ and printout methods to conform with
    #       the new bahavior of the class.


    def __init__(self,char_name,points):
        self.name = char_name
        #find were points is needed
        self.point = points
        #creating class variables so they can store methods value swhich are needed
        self.itemlist = []
        self.items = ""
        self.has = ""


    def printout(self):
        print(f"Name: {self.name}")
        print(f"Hitpoints: {self.point}")

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


    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """

        # TODO: implementation of the method

        if item in self.itemlist:
            target.itemlist.append(item)
            self.itemlist.remove(item)
            return True
        else:
            return False

    # conan.attack(deadpool, "sword")
    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """


        # TODO: the implementation of the method

        if self.name == target.name and weapon in WEAPONS:
            print(f"Attack fails: {target.name} can't attack him/herself.")

        if weapon not in WEAPONS:
            #print(f"Attack fails: unknown weapon {weapon}.")
            print('Attack fails: unknown weapon "'+weapon+'".')

        elif weapon not in self.itemlist:
            print(f"Attack fails: {self.name} doesn't have \"{weapon}\".")
            #print('Attack fails: '+self.name+' doesn't have "'+weapon+'".')


        if weapon in self.itemlist and self.name != target.name:
            """damage = WEAPONS[weapon]
            damage_counter += damage
            drop_bar = self.point - damage
            self.point-=drop_bar
            print(f"{self.name} attacks {target.name} delivering {WEAPONS[weapon]} damage.")
            if self.point <= damage_counter:
                print(f"{self.name} successfully defeats {target.name}.")"""

            damage = WEAPONS[weapon]

            target.point = target.point - damage
            print(f"{self.name} attacks {target.name} delivering {WEAPONS[weapon]} damage.")
            if target.point <= 0:
                print(f"{self.name} successfully defeats {target.name}.")

#conan.attack(deadpool, "sword")

WEAPONS = {
    # Weapon          Damage
    #--------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)


    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()


    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword") # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword") # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
