"""
-------------------------------------------------
File: template_method.py
Intent: 
    Template Method is a behavioral design pattern that defines
    the skeleton of an algorithm in the superclass but lets subclasses
    override specific steps of the algorithm without changing its structure.

Usage:
    Use the Template Method pattern when you
    want to let clients extend only particular steps
    of an algorithm, but not the whole algorithm or its structure.
-------------------------------------------------
"""

from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def process(self, data):
        self.validate_data(data)
        transformed_data = self.transform_data(data)
        self.store_data(transformed_data)

    @abstractmethod
    def validate_data(self, data):
        pass

    @abstractmethod
    def transform_data(self, data):
        pass

    @abstractmethod
    def store_data(self, data):
        pass


class JSONDataProcessor(DataProcessor):

    def validate_data(self, data):
        print("Validating JSON data...")
        if not isinstance(data, dict):
            raise ValueError(
                "Invalid JSON data format. Expected a dictionary.")

    def transform_data(self, data):
        print("Transforming JSON data...")
        return {
            k: v.upper() if isinstance(v, str) else v
            for k, v in data.items()
        }

    def store_data(self, data):
        print("Storing JSON data...")
        print("Data saved:", data)


def template_json_method():
    json_data = {"name": "John", "age": 30, "city": "New York"}
    json_processor = JSONDataProcessor()
    json_processor.process(json_data)
