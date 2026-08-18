def buggy_add_item(item, cart=[]):
    cart.append(item)
    return cart

print("PART A - Mutable Default Argument Bug")
print(buggy_add_item("apple"))
print(buggy_add_item("banana"))
print(buggy_add_item("milk", cart=["bread"]))
print(buggy_add_item("eggs"))

def add_item(item, cart=None):
    """Add an item to a fresh cart when no cart is supplied."""
    if cart is None:
        cart = []

    cart.append(item)
    return cart

print("\nPART B - Correct Function")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

def create_cart(owner, discount=0):
    """Create and return an independent shopping cart."""
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }

def add_to_cart(cart, name, price, qty=1):
    """Add a product to the cart."""
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })

def update_price(price_tuple, new_price):
    """Demonstrate that tuple elements cannot be changed."""
    try:
        price_tuple[1] = new_price
    except TypeError as error:
        print("Tuple modification failed:", error)
        print("Reason: tuples are immutable and cannot be changed.")

def calculate_total(cart):
    """Calculate total after applying the discount percentage."""
    subtotal = 0

    for item in cart["items"]:
        subtotal += item["price"] * item["qty"]

    discount_amount = subtotal * cart["discount"] / 100
    final_total = subtotal - discount_amount

    return final_total

def display_cart(cart):
    """Display all details of a shopping cart."""
    print(f"\nCustomer: {cart['owner']}")
    print(f"Discount: {cart['discount']}%")

    print("Items:")
    for item in cart["items"]:
        item_total = item["price"] * item["qty"]
        print(
            f"- {item['name']} | "
            f"Price: {item['price']:.2f} | "
            f"Quantity: {item['qty']} | "
            f"Total: {item_total:.2f}"
        )

    print(f"Final Total: {calculate_total(cart):.2f}")

def main():
   
    cart1 = create_cart("Aarav", discount=10)
    cart2 = create_cart("Priya", discount=5)

    add_to_cart(cart1, "Laptop Bag", 1500, 1)
    add_to_cart(cart1, "Notebook", 100, 3)

    add_to_cart(cart2, "Headphones", 2000, 1)
    add_to_cart(cart2, "Pen Drive", 800, 2)

    display_cart(cart1)
    display_cart(cart2)

    print("\nIndependence check:")
    print("Cart 1 items:", cart1["items"])
    print("Cart 2 items:", cart2["items"])

    add_to_cart(cart1, "Water Bottle", 500, 1)

    print("\nAfter adding an item only to Cart 1:")
    print("Cart 1 items:", cart1["items"])
    print("Cart 2 items:", cart2["items"])

    price_tuple = ("Laptop", 50000)
    print("\nTuple before modification:", price_tuple)
    update_price(price_tuple, 45000)
    print("Tuple after attempted modification:", price_tuple)

if __name__ == "__main__":
    main()
