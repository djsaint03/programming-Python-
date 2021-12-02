"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:  150421047
Name: Johnson Apanishile
Email:johnson.apansihile@tuni.fi

Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    col_store= input("Enter product name: ")
    store= col_store.strip()

    while True:
            if store not in PRICES and store != "" and store != " ":
                print(f"Error: {store} is unknown.")
                col_store= input("Enter product name: ")
                store= col_store.strip()

            elif store in PRICES:
                x = PRICES[store]
                print(f"The price of {store} is {x:.2f} e")
                col_store = input("Enter product name: ")
                store = col_store.strip()

            elif store == " " or store == "":
                print("Bye!")
                break


"""
    if store == " " or store == "":
        print("Bye!")

    elif store in PRICES:
        x = PRICES[store]
        print(f"The price of milk is {x} e ")
"""




if __name__ == "__main__":
    main()
