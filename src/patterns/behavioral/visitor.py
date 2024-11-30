"""
-------------------------------------------------
File: visitor.py
Intent: 
    Visitor is a behavioral design
    pattern that lets you separate
    algorithms from the objects on which they operate.

Usage:
    Use the Visitor when you need
    to perform an operation on all elements of
    a complex object structure (for example, an object tree).
-------------------------------------------------
"""

from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_electronics(self, electronics):
        pass

    @abstractmethod
    def visit_groceries(self, groceries):
        pass

    @abstractmethod
    def visit_clothing(self, clothing):
        pass

class Visitable(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

class Electronics(Visitable):
    def __init__(self, price: float, warranty_years: int):
        self.price = price
        self.warranty_years = warranty_years

    def accept(self, visitor: Visitor):
        visitor.visit_electronics(self)

class Groceries(Visitable):
    def __init__(self, price: float, weight: float):
        self.price = price
        self.weight = weight

    def accept(self, visitor: Visitor):
        visitor.visit_groceries(self)

class Clothing(Visitable):
    def __init__(self, price: float, brand: str):
        self.price = price
        self.brand = brand

    def accept(self, visitor: Visitor):
        visitor.visit_clothing(self)

class DiscountVisitor(Visitor):
    def visit_electronics(self, electronics: Electronics):
        discount = 0.1 if electronics.warranty_years > 2 else 0.05
        final_price = electronics.price * (1 - discount)
        print(f"Electronics: Original Price = ${electronics.price:.2f}, Discounted Price = ${final_price:.2f}")

    def visit_groceries(self, groceries: Groceries):
        discount = 0.05 if groceries.weight > 5 else 0.02
        final_price = groceries.price * (1 - discount)
        print(f"Groceries: Original Price = ${groceries.price:.2f}, Discounted Price = ${final_price:.2f}")

    def visit_clothing(self, clothing: Clothing):
        discount = 0.15 if clothing.brand == "Premium" else 0.1
        final_price = clothing.price * (1 - discount)
        print(f"Clothing: Original Price = ${clothing.price:.2f}, Discounted Price = ${final_price:.2f}")

class TaxVisitor(Visitor):
    def visit_electronics(self, electronics: Electronics):
        tax_rate = 0.18
        tax = electronics.price * tax_rate
        print(f"Electronics: Price = ${electronics.price:.2f}, Tax = ${tax:.2f}")

    def visit_groceries(self, groceries: Groceries):
        tax_rate = 0.05
        tax = groceries.price * tax_rate
        print(f"Groceries: Price = ${groceries.price:.2f}, Tax = ${tax:.2f}")

    def visit_clothing(self, clothing: Clothing):
        tax_rate = 0.12
        tax = clothing.price * tax_rate
        print(f"Clothing: Price = ${clothing.price:.2f}, Tax = ${tax:.2f}")

def main():
    items = [
        Electronics(price=1200, warranty_years=3),
        Groceries(price=50, weight=6),
        Clothing(price=100, brand="Premium"),
    ]

    discount_visitor = DiscountVisitor()
    tax_visitor = TaxVisitor()

    print("Applying Discount Visitor:")
    for item in items:
        item.accept(discount_visitor)

    print("\nApplying Tax Visitor:")
    for item in items:
        item.accept(tax_visitor)
