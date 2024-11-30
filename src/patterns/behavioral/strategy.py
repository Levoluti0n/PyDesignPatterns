"""
-------------------------------------------------
File: strategy.py
Intent: 
    Strategy is a behavioral design pattern thatlets
    you define a family of algorithms, put each of them
    into a separate class, and make their objects interchangeable.

Usage:
    Use the Strategy pattern when you want to use
    different variants of an algorithm within an object
    and be able to switch from one algorithm to another during runtime.
-------------------------------------------------
"""

from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass


class CreditCardPayment(PaymentStrategy):

    def __init__(self, card_number: str, card_holder_name: str, cvv: str):
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.cvv = cvv

    def pay(self, amount: float):
        print(
            f"Processing credit card payment of ${amount:.2f} for card holder '{self.card_holder_name}' using card number '{self.card_number[-4:]}'..."
        )


class PayPalPayment(PaymentStrategy):

    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float):
        print(
            f"Processing PayPal payment of ${amount:.2f} for user '{self.email}'..."
        )


class CryptoPayment(PaymentStrategy):

    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float):
        print(
            f"Processing cryptocurrency payment of ${amount:.2f} to wallet '{self.wallet_address[:6]}...'..."
        )


class PaymentProcessor:

    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def process_payment(self, amount: float):
        if not self._strategy:
            print("No payment strategy set!")
            return
        self._strategy.pay(amount)


def pay_strategy():
    credit_card = CreditCardPayment("1234567890123456", "Alice Johnson", "123")
    paypal = PayPalPayment("alice.johnson@example.com")
    crypto = CryptoPayment("1FfmbHfnpaZjKFvyi1okTjJJusN455paPH")

    processor = PaymentProcessor(None)

    print("Selecting credit card payment...")
    processor.set_strategy(credit_card)
    processor.process_payment(150.75)

    print("\nSelecting PayPal payment...")
    processor.set_strategy(paypal)
    processor.process_payment(89.99)

    print("\nSelecting cryptocurrency payment...")
    processor.set_strategy(crypto)
    processor.process_payment(0.015)
