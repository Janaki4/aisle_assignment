from math import ceil

def round_up_to_nearest_0_05(amount: float) -> float:
    return ceil(amount * 20) / 20

def calculate_tax(price: float, tax_rate: float) -> float:
    tax = price * tax_rate / 100
    return round_up_to_nearest_0_05(tax)