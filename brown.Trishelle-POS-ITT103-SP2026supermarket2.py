# ==========================================
# POINT OF SALE (POS) SYSTEM
# Course: ITT103
# Author:Trishelle Brown
# ==========================================

# -------------------------------
# PRODUCT CATALOG (Dictionary)
# -------------------------------
products = {
    "rice": {"price": 120, "stock": 20},
    "flour": {"price": 100, "stock": 15},
    "milk": {"price": 150, "stock": 10},
    "bread": {"price": 180, "stock": 12},
    "eggs": {"price": 300, "stock": 8},
    "juice": {"price": 200, "stock": 9},
    "soap": {"price": 90, "stock": 25},
    "toothpaste": {"price": 250, "stock": 6},
    "oil": {"price": 600, "stock": 7},
    "sugar": {"price": 130, "stock": 14}
}

# Shopping cart (stores items selected)
cart = {}


# -------------------------------
# DISPLAY MENU
# -------------------------------
def display_menu():
    print("\n====== BEST BUY POS SYSTEM ======")
    print("1. View Products")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")


# -------------------------------
# VIEW PRODUCTS
# -------------------------------
def view_products():
    print("\n--- PRODUCT LIST ---")
    for item, details in products.items():
        print(f"{item.capitalize()} - Price: ${details['price']} | Stock: {details['stock']}")


# -------------------------------
# ADD TO CART
# -------------------------------
def add_to_cart():
    item = input("Enter product name: ").lower()

    if item not in products:
        print("Item not found!")
        return

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity!")
        return

    if qty <= 0:
        print("Quantity must be greater than 0")
        return

    if qty > products[item]["stock"]:
        print("Not enough stock available!")
        return

    # Add to cart
    if item in cart:
        cart[item] += qty
    else:
        cart[item] = qty

    products[item]["stock"] -= qty

    print(f"{item} added to cart successfully!")

    # Low stock alert
    if products[item]["stock"] < 5:
        print(f"? WARNING: Low stock for {item}!")


# -------------------------------
# REMOVE FROM CART
# -------------------------------
def remove_from_cart():
    item = input("Enter item to remove: ").lower()

    if item not in cart:
        print("Item not in cart!")
        return

    qty = int(input("Enter quantity to remove: "))

    if qty >= cart[item]:
        products[item]["stock"] += cart[item]
        del cart[item]
    else:
        cart[item] -= qty
        products[item]["stock"] += qty

    print("Item removed successfully!")


# -------------------------------
# VIEW CART
# -------------------------------
def view_cart():
    print("\n--- SHOPPING CART ---")

    if not cart:
        print("Cart is empty!")
        return

    total = 0

    for item, qty in cart.items():
        price = products[item]["price"]
        item_total = price * qty
        total += item_total

        print(f"{item.capitalize()} | Qty: {qty} | Unit: ${price} | Total: ${item_total}")

    print(f"Subtotal: ${total}")


# -------------------------------
# CHECKOUT FUNCTION
# -------------------------------
def checkout():
    if not cart:
        print("Cart is empty!")
        return

    subtotal = 0

    # Calculate subtotal
    for item, qty in cart.items():
        subtotal += products[item]["price"] * qty

    # Apply discount
    discount = 0
    if subtotal > 5000:
        discount = subtotal * 0.05

    subtotal_after_discount = subtotal - discount

    # Apply tax (10%)
    tax = subtotal_after_discount * 0.10
    total = subtotal_after_discount + tax

    print("\n------ BILL SUMMARY ------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax (10%): ${tax:.2f}")
    print(f"TOTAL: ${total:.2f}")

    # Payment validation
    while True:
        try:
            payment = float(input("Enter amount paid: $"))
            if payment < total:
                print("Insufficient payment! Try again.")
            else:
                break
        except ValueError:
            print("Invalid input!")

    change = payment - total

    # Print receipt
    print_receipt(subtotal, discount, tax, total, payment, change)

    # Clear cart for next transaction
    cart.clear()


# -------------------------------
# PRINT RECEIPT
# -------------------------------
def print_receipt(subtotal, discount, tax, total, payment, change):
    print("\n=========== RECEIPT ===========")
    print("Best Buy Retail Store")
    print("-------------------------------")

    for item, qty in cart.items():
        price = products[item]["price"]
        print(f"{item.capitalize()} x{qty} - ${price * qty}")

    print("-------------------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"TOTAL: ${total:.2f}")
    print(f"Paid: ${payment:.2f}")
    print(f"Change: ${change:.2f}")
    print("\nThank you for shopping with us!")
    print("================================")


# -------------------------------
# MAIN PROGRAM LOOP
# -------------------------------
def main():
    while True:
        display_menu()

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            view_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


# Run program
main()