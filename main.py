from input_parser import parse_input
from shopping_cart import ShoppingCart

def process_and_print(inputs):
    for i, item_list in enumerate(inputs, 0):
        products = parse_input(item_list)
        cart = ShoppingCart()
        for product in products:
            cart.add_product(product)
        receipt = cart.generate_receipt()
        print(f"Output {i}:")
        print(receipt.format())
        print()

if __name__ == "__main__":
    inputs = [
        [
            {"name": "book", "quantity": 1, "price": 12.49, "imported": False},
            {"name": "music CD", "quantity": 1, "price": 14.99, "imported": False},
            {"name": "chocolate bar", "quantity": 1, "price": 0.85, "imported": False}
        ],
        [
            {"name": "imported box of chocolates", "quantity": 1, "price": 10.00, "imported": True},
            {"name": "imported bottle of perfume", "quantity": 1, "price": 47.50, "imported": True}
        ],
        [
            {"name": "imported bottle of perfume", "quantity": 1, "price": 27.99, "imported": True},
            {"name": "bottle of perfume", "quantity": 1, "price": 18.99, "imported": False},
            {"name": "packet of headache pills", "quantity": 1, "price": 9.75, "imported": False},
            {"name": "box of imported chocolates", "quantity": 1, "price": 11.25, "imported": True}
        ]
    ]
    process_and_print(inputs)
