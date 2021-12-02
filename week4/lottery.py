"""
Programming 1 course
this program was written bby Johnson Apanishile
"""

def lot_prob(lot_balls, drwn_balls):
    """
    this functions calculates the factorial of the given
    parameters
    """
    fact_lot_balls = 1
    fact_drw_balls = 1
    need_fact=1

    for x in range(1,lot_balls+1):
        fact_lot_balls = fact_lot_balls*x
    for y in range(1,drwn_balls+1):
        fact_drw_balls = fact_drw_balls*y
    need= lot_balls-drwn_balls
    for z in range(1,need+1):
        need_fact= need_fact*z

    cal1= (need_fact)*fact_drw_balls
    cal= int(fact_lot_balls/cal1)
    return cal


def lottery_condition(lot_balls, drwn_balls):
    """
    this function creates a condition for the efective selection of lottery numbers
    """

    if lot_balls <=0 or drwn_balls <=0:
        return print("The number of balls must be a positive number. ")

    elif drwn_balls >= lot_balls:
        return print("At most the total number of balls can be drawn.")

    else:
        return print(f"The probability of guessing all {drwn_balls} balls correctly is 1/{lot_prob(lot_balls, drwn_balls)}")


def main():

    lotter_balls = int(input("Enter the total number of lottery balls: "))
    drawn_balls = int(input("Enter the number of the drawn balls: "))
    lottery_condition(lotter_balls, drawn_balls)




if __name__ == "__main__":
    main()