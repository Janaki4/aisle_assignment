from typing import List
from product import Product

class Receipt:
    def __init__(self, products: List[Product]):
        self.products = products

    def total_sales_taxes(self) -> float:
        total_tax = 0.0
        for p in self.products:
            total_tax += p.calculate_tax() * p.quantity
        return total_tax

    def total_price(self) -> float:
        total = 0.0
        for p in self.products:
            total += p.total_price_with_quantity()
        return total

    def format(self) -> str:
        lines = []
        for p in self.products:
            lines.append(f"{p.quantity} {p.name}: {p.total_price_with_quantity()}")
        lines.append(f"Sales Taxes: {self.total_sales_taxes()}")
        lines.append(f"Total: {self.total_price()}")
        return "\n".join(lines)
