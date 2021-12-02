"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""


# TODO:
# a) Implement the class Player here.

class Player:

    def __init__(self, name):
        self.__name = name
        self.__int_points = 0
        self.__rounds = 0
        self.__counter = 0
        self.__percent = 100


    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__int_points

    def add_points(self, points):
        self.__int_points += points
        self.__rounds += 1

        if points > 0:
            self.__counter += 1 #when each person has gain point > 0, they will have +1

        #if the points is greater than 50 then change to 25points
        if self.__int_points > 50:
            self.__int_points = 25
            print(f"{self.__name} gets penalty points!")
            return self.__int_points

        #if if the points is greater than 40 and lest than 50 print meesage
        if self.__int_points >= 40 and self.__int_points <= 49:
            print(f"{self.__name} needs only {50 - self.__int_points} points. It's better to avoid knocking down the pins with higher points.")
        else:
            return self.__int_points

    def average(self):
        avg= self.__int_points /self.__rounds
        return avg

    def percentage(self):
        if self.__rounds == 0:
            return 0.0

        else:
            result = f"{(self.__counter/self.__rounds)*100:.1f}"
            return result


    def has_won(self):
        if self.__int_points == 50:
            return True



def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.
        if in_turn.average() < pts:
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p, hit percentage", player1.percentage())  # TODO: d)
        print(player2.get_name() + ":", player2.get_points(), "p, hit percentage", player2.percentage())  # TODO: d)
        print("")

        throw += 1


if __name__ == "__main__":
    main()