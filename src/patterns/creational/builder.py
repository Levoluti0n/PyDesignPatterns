"""
-------------------------------------------------
File: builder.py
Intent: 
    Builder is a creational design pattern that lets you construct
    complex objects step by step. The pattern allows you to produce different
    types and representations of an object using the same construction code.
    
Usage:
    Use the Builder pattern to get rid of a “telescoping constructor”.
-------------------------------------------------
"""

from abc import ABC, abstractmethod

class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.doors = None
        self.color = None

    def __str__(self):
        return f"Car with Engine: {self.engine}, Wheels: {self.wheels}, Doors: {self.doors}, Color: {self.color}"
    
class CarBuilder(ABC):
    @abstractmethod
    def set_engine(self, engine: str):
        pass

    @abstractmethod
    def set_wheels(self, wheels: int):
        pass

    @abstractmethod
    def set_doors(self, doors: int):
        pass

    @abstractmethod
    def set_color(self, color: str):
        pass

    @abstractmethod
    def get_result(self) -> Car:
        pass

class SedanCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_engine(self, engine: str):
        self.car.engine = engine
        return self

    def set_wheels(self, wheels: int):
        self.car.wheels = wheels
        return self

    def set_doors(self, doors: int):
        self.car.doors = doors
        return self

    def set_color(self, color: str):
        self.car.color = color
        return self

    def get_result(self) -> Car:
        return self.car
    
class SuvCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_engine(self, engine: str):
        self.car.engine = engine
        return self

    def set_wheels(self, wheels: int):
        self.car.wheels = wheels
        return self

    def set_doors(self, doors: int):
        self.car.doors = doors
        return self

    def set_color(self, color: str):
        self.car.color = color
        return self

    def get_result(self) -> Car:
        return self.car

class CarDirector:
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def construct_sedan(self):
        return (self.builder
                .set_engine("V6 Engine")
                .set_wheels(4)
                .set_doors(4)
                .set_color("Black")
                .get_result())

    def construct_suv(self):
        return (self.builder
                .set_engine("V8 Engine")
                .set_wheels(4)
                .set_doors(5)
                .set_color("Silver")
                .get_result())
