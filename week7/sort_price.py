"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150421047
Name: Johnson apanishile
Email: johnson.apanishile@tuni.fi

Template for sorting by price assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    new_val = PRICES.values()
    val = sorted(list(new_val))
    keyss = PRICES.keys()

    for x in val:
        for key, value in PRICES.items():
            if x == value:
                print(f"{key} {x:.2f}")




if __name__ == "__main__":
    main()
