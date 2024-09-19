# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    # Sort products by price
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))

def display_products(products_list):
    # Display products in a numbered format
    print("Products available:")
    for idx, (name, price) in enumerate(products_list, start=1):
        print(f"{idx}. {name} - ${price:.2f}")

def display_categories():
    # Display categories in a numbered format
    print("Categories available:")
    for idx, category in enumerate(products.keys(), start=1):
        print(f"{idx}. {category}")

def add_to_cart(cart, product, quantity):
    # Add products to the cart
    cart.append({'product': product, 'quantity': quantity})

def display_cart(cart):
    # Display the cart contents
    print("\n--- Shopping Cart ---")
    for item in cart:
        product_name, product_price = item['product']
        print(f"{item['quantity']} x {product_name} - ${product_price:.2f} each")

def generate_receipt(name, email, cart, total_cost, address):
    # Generate and display the receipt
    print("\n--- Receipt ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("\nItems Purchased:")
    for item in cart:
        product_name, product_price = item['product']
        print(f"{item['quantity']} x {product_name} - ${product_price:.2f} each")
    print(f"\nTotal Cost: ${total_cost:.2f}")
    print(f"Delivery Address: {address}")
    print("\nYour items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    # Validate the name: must contain only alphabets and have a first and last name
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    # Validate the email: must contain '@'
    return '@' in email

def main():
    # Get user information
    name = input("Enter your full name: ")
    while not validate_name(name):
        print("Invalid name. Please enter both first and last name containing only alphabets.")
        name = input("Enter your full name: ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email containing '@'.")
        email = input("Enter your email address: ")

    # Shopping logic
    cart = []
    total_cost = 0
    while True:
        display_categories()
        try:
            category_choice = int(input("\nSelect a category by number: "))
            category_list = list(products.keys())
            if category_choice < 1 or category_choice > len(category_list):
                print("Invalid category choice. Please try again.")
                continue

            category_name = category_list[category_choice - 1]
            product_list = products[category_name]
            while True:
                display_products(product_list)
                print("\nOptions:")
                print("1. Select a product to buy")
                print("2. Sort the products according to the price")
                print("3. Go back to the category selection")
                print("4. Finish shopping")
                
                try:
                    option = int(input("\nSelect an option: "))

                    if option == 1:
                        product_choice = int(input("Enter the product number to buy: "))
                        if product_choice < 1 or product_choice > len(product_list):
                            print("Invalid product choice. Please try again.")
                            continue
                        product = product_list[product_choice - 1]

                        while True:
                            try:
                                quantity = int(input("Enter quantity: "))
                                if quantity <= 0:
                                    print("Quantity must be a positive number. Please try again.")
                                else:
                                    break
                            except ValueError:
                                print("Invalid input. Please enter a valid quantity.")

                        add_to_cart(cart, product, quantity)
                        total_cost += product[1] * quantity
                        print(f"Added {quantity} x {product[0]} to cart.\n")

                    elif option == 2:
                        while True:
                            try:
                                sort_order = int(input("Sort by price: 1. Ascending 2. Descending: "))
                                if sort_order not in [1, 2]:
                                    print("Invalid sort order. Please enter 1 or 2.")
                                    continue
                                break
                            except ValueError:
                                print("Invalid input. Please enter a number.")
                        
                        sorted_products = display_sorted_products(product_list, sort_order)
                        display_products(sorted_products)

                    elif option == 3:
                        break

                    elif option == 4:
                        if cart:
                            display_cart(cart)
                            address = input("Enter the delivery address: ")
                            generate_receipt(name, email, cart, total_cost, address)
                        else:
                            print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                        return
                    else:
                        print("Invalid option. Please try again.")

                except ValueError:
                    print("Invalid input. Please enter a number.")

        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the program
if __name__ == "__main__":
    main()
