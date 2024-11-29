"""
-------------------------------------------------
File: adapter.py
Intent: 
    Adapter is a structural design pattern that allows
    objects with incompatible interfaces to collaborate.

Usage:
    Use the Adapter class when you want to use some existing class,
    but its interface isn't compatible with the rest of your code.
-------------------------------------------------
"""

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class StripePayment:

    def make_payment(self, amount):
        print(f"Processing payment of ${amount} via Stripe.")


class StripeAdapter(PaymentProcessor):

    def __init__(self, stripe):
        self.stripe = stripe

    def pay(self, amount):
        self.stripe.make_payment(amount)


def process_payment(amount):
    payment_processor = StripePayment()
    stripe_adapter = StripeAdapter(payment_processor)
    print("Stripe Adapter Created!")
    stripe_adapter.pay(amount)
