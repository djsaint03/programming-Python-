PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}

def main():
    product_name = input("Enter product name: ")
    new_product_name = product_name.strip()
    valid_input = True
    while valid_input:

        if product_name in PRICES:
            print(f"The price of product is {PRICES[product_name]} e")

        elif product_name not in PRICES:
            print(f"Error: {product_name} is unknown.")
        elif product_name:
            valid_input = False
            print("Bye!")


if __name__ == "__main__":
    main()