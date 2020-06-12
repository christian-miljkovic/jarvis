add_item_success = (
    lambda cart_item_dict_name, quantity: f"You've successfully added {quantity} {cart_item_dict_name} to your cart! Reply with `Checkout` if you're done shopping!\n"
)
shopping_cart_info = (
    lambda shopping_cart_size: f"Shopping cart ({shopping_cart_size})\n"
)
