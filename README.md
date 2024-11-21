# Design Patterns in Python 🐍

This repository contains implementations of various **Design Patterns** in Python, following the principles from [Refactoring Guru](https://refactoring.guru/design-patterns). Design patterns are reusable solutions to common problems in software design. Each pattern is implemented in its respective category, and the code is structured for easy integration into your Python projects.

## Table of Contents 📑

- [Creational Patterns](#creational-patterns) 🏗️
  - [Singleton](#singleton) 🔒
  - [Factory Method](#factory-method) 🏭
  - [Abstract Factory](#abstract-factory) 🏢
  - [Builder](#builder) 🛠️
  - [Prototype](#prototype) 🌱
- [Structural Patterns](#structural-patterns) 🏛️
  - [Adapter](#adapter) ⚙️
  - [Bridge](#bridge) 🌉
  - [Composite](#composite) 🧩
  - [Decorator](#decorator) 🎨
  - [Facade](#facade) 🏠
  - [Flyweight](#flyweight) 🦋
  - [Proxy](#proxy) 🕵️‍♂️
- [Behavioral Patterns](#behavioral-patterns) 🧠
  - [Chain of Responsibility](#chain-of-responsibility) ⛓️
  - [Command](#command) 📜
  - [Interpreter](#interpreter) 🗣️
  - [Iterator](#iterator) 🔄
  - [Mediator](#mediator) 🤝
  - [Memento](#memento) 🕰️
  - [Observer](#observer) 👀
  - [State](#state) 🔄
  - [Strategy](#strategy) 🎯
  - [Template Method](#template-method) 📝
  - [Visitor](#visitor) 🧳

---

## Creational Patterns 🏗️

### Singleton 🔒
The **Singleton** pattern ensures that a class has only one instance and provides a global point of access to it. It is often used to manage resources that should have only one instance, such as a database connection.

### Factory Method 🏭
The **Factory Method** pattern defines an interface for creating objects, but allows subclasses to alter the type of objects that will be created. It helps in creating objects without specifying the exact class of object that will be created.

### Abstract Factory 🏢
The **Abstract Factory** pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. It is useful for creating objects that belong to a specific theme or category.

### Builder 🛠️
The **Builder** pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

### Prototype 🌱
The **Prototype** pattern creates new objects by copying an existing object, known as the prototype. It is used when creating a new instance of an object is costly or complicated.

---

## Structural Patterns 🏛️

### Adapter ⚙️
The **Adapter** pattern allows incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces, enabling them to collaborate.

### Bridge 🌉
The **Bridge** pattern decouples an abstraction from its implementation, allowing them to vary independently. It is useful when both the abstractions and their implementations should be extended.

### Composite 🧩
The **Composite** pattern allows you to compose objects into tree-like structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions uniformly.

### Decorator 🎨
The **Decorator** pattern allows you to attach new behaviors to an object dynamically, without altering its structure. It is useful for extending functionality in a flexible and reusable way.

### Facade 🏠
The **Facade** pattern provides a simplified interface to a complex system of classes, libraries, or frameworks. It hides the complexities of the system and provides a higher-level interface.

### Flyweight 🦋
The **Flyweight** pattern reduces the number of objects created by sharing common objects instead of creating new ones. It is used to reduce memory usage by sharing objects.

### Proxy 🕵️‍♂️
The **Proxy** pattern provides a surrogate or placeholder for another object. It controls access to the original object, which may involve additional functionality such as lazy initialization, access control, or logging.

---

## Behavioral Patterns 🧠

### Chain of Responsibility ⛓️
The **Chain of Responsibility** pattern allows you to pass a request along a chain of handlers, each of which can either process the request or pass it along to the next handler.

### Command 📜
The **Command** pattern encapsulates a request as an object, thereby allowing for parameterization of clients with different requests. It decouples the sender and receiver of the request.

### Interpreter 🗣️
The **Interpreter** pattern defines a grammatical representation for a language and provides an interpreter to evaluate sentences in the language. It is used for implementing expression evaluation.

### Iterator 🔄
The **Iterator** pattern provides a way to sequentially access elements of a collection without exposing its underlying representation.

### Mediator 🤝
The **Mediator** pattern defines an object that encapsulates how a set of objects interact. It centralizes communication between objects, promoting loose coupling.

### Memento 🕰️
The **Memento** pattern captures and externalizes an object's internal state, allowing it to be restored later without violating encapsulation.

### Observer 👀
The **Observer** pattern allows a subject to notify its observers of state changes. It is commonly used in event-driven systems where multiple components need to be updated when an event occurs.

### State 🔄
The **State** pattern allows an object to change its behavior when its internal state changes. The object appears to change its class when its state changes.

### Strategy 🎯
The **Strategy** pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It allows the algorithm to be selected at runtime.

### Template Method 📝
The **Template Method** pattern defines the skeleton of an algorithm, deferring steps of the algorithm to subclasses. It lets subclasses redefine certain steps without changing the algorithm's structure.

### Visitor 🧳
The **Visitor** pattern allows you to define new operations on elements of an object structure without changing the classes of the elements. It helps in separating the logic from the structure.

---

## Installation 🛠️

To start the program, run the following command:

```bash
cd ./scripts
./start.sh
