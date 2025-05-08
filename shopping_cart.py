from typing import List
from product import Product
from receipt import Receipt

class ShoppingCart:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def generate_receipt(self) -> Receipt:
        return Receipt(self.products)

