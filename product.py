from tax import calculate_tax

class Product:
    def __init__(self, name: str, price: float, quantity: int, is_imported: bool = False):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_imported = is_imported

    def is_exempt_from_basic_tax(self) -> bool:
        exempt_keywords = ["book", "chocolate", "pill"]
        name_lower = self.name.lower()
        for keyword in exempt_keywords:
            if keyword in name_lower:
                return True
        return False

    def calculate_tax(self) -> float:
        tax = 0.0
        if not self.is_exempt_from_basic_tax():
            tax += calculate_tax(self.price, 10.0)
        if self.is_imported:
            tax += calculate_tax(self.price, 5.0)
        return tax

    def total_price(self) -> float:
        return self.price + self.calculate_tax()

    def total_price_with_quantity(self) -> float:
        return self.total_price() * self.quantity

