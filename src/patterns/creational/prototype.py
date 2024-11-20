"""
-------------------------------------------------
File: prototype.py
Intent: 
    Prototype is a creational design pattern that lets you copy
    existing objects without making your code dependent on their classes.
    
Usage:
    Use the pattern when you want to reduce the number of subclasses
    that only differ in the way they initialize their respective objects.
-------------------------------------------------
"""

import copy
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def display(self):
        pass 

class TextDocument(Document):
    def __init__(self, content: str):
        self.content = content

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print(f"TextDocument Content: {self.content}")

class SpreadsheetDocument(Document):
    def __init__(self, data: list):
        self.data = data

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print(f"SpreadsheetDocument Data: {self.data}")

def create_document_clone(document: Document):
    clone = document.clone()
    return clone
