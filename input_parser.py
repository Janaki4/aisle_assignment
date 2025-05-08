from typing import List, Dict
from product import Product

def parse_input(input_data: List[Dict]) -> List[Product]:
    products = []
    for item in input_data:
        product = Product(
            name=item["name"],
            price=item["price"],
            quantity=item["quantity"],
            is_imported=item.get("imported", False)
        )
        products.append(product)
    return products
