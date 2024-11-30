"""
-------------------------------------------------
File: observer.py
Intent: 
    Observer is a behavioral design pattern that lets you
    define a subscription mechanism to notify multiple objects
    about any events that happen to the object they're observing.

Usage:
    Use the pattern when some objects
    in your app must observe others, but
    only for a limited time or in specific cases.
-------------------------------------------------
"""

from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):

    def __init__(self):
        self._observers: List[Observer] = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    @abstractmethod
    def notify(self):
        pass


class Stock(Subject):

    def __init__(self, symbol: str, price: float):
        super().__init__()
        self._symbol = symbol
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, price: float):
        if price != self._price:
            self._price = price
            self.notify()

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def get_symbol(self):
        return self._symbol


class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject):
        pass


class StockTrader(Observer):

    def __init__(self, name: str, threshold: float):
        self.name = name
        self.threshold = threshold

    def update(self, subject: Subject):
        if isinstance(subject, Stock):
            if subject.get_price() > self.threshold:
                print(
                    f"Trader {self.name}: Stock {subject.get_symbol()} price has crossed the threshold! Price: {subject.get_price()}"
                )


class StockPriceAlert(Observer):

    def __init__(self, alert_message: str):
        self.alert_message = alert_message

    def update(self, subject: Subject):
        if isinstance(subject, Stock):
            print(
                f"Alert: {self.alert_message} - {subject.get_symbol()} New Price: {subject.get_price()}"
            )


class StockInvestmentTracker(Observer):

    def __init__(self, initial_investment: float):
        self.total_investment = initial_investment

    def update(self, subject: Subject):
        if isinstance(subject, Stock):
            investment_value = subject.get_price() * 100
            print(
                f"Investment Tracker: New total investment value in {subject.get_symbol()} is: {investment_value}"
            )


def stock_observer():
    stock = Stock("AAPL", 150.00)

    trader1 = StockTrader("Alice", 160.00)
    alert_system = StockPriceAlert("Price Alert Triggered")
    investment_tracker = StockInvestmentTracker(10000.00)

    stock.add_observer(trader1)
    stock.add_observer(alert_system)
    stock.add_observer(investment_tracker)

    print("Changing stock price to 155.00")
    stock.set_price(165.00)
