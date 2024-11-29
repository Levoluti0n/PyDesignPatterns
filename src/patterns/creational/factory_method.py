"""
-------------------------------------------------
File: factory_method.py
Intent: 
    Factory Method is a creational design pattern that provides an interface for creating
    object in a superclass, but allows subclasses to alter the type of objects that will be created.
    
Usage:
    Use the Factory Method when you don't know beforehand the exact
    types and dependencies of the objects your code should work with.
-------------------------------------------------
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    name = "Car"

    def drive(self):
        return "Driving a Car"


class Bike(Vehicle):
    name = "Bike"

    def drive(self):
        return "Riding a Bike"


class Truck(Vehicle):
    name = "Truck"

    def drive(self):
        return "Driving a Truck"


class VehicleFactory(ABC):

    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass


class CarFactory(VehicleFactory):

    def create_vehicle(self) -> Vehicle:
        return Car()


class BikeFactory(VehicleFactory):

    def create_vehicle(self) -> Vehicle:
        return Bike()


class TruckFactory(VehicleFactory):

    def create_vehicle(self) -> Vehicle:
        return Truck()


def get_vehicle_to_drive(vehicle_type: str):
    if vehicle_type == 'car':
        factory = CarFactory()
    elif vehicle_type == 'bike':
        factory = BikeFactory()
    elif vehicle_type == 'truck':
        factory = TruckFactory()
    else:
        raise ValueError(f"Unknown vehicle type: {vehicle_type}")

    vehicle = factory.create_vehicle()
    print(f"Created Vehicles: {vehicle.name}")
    print(vehicle.drive(), '\n')
