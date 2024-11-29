"""
-------------------------------------------------
File: abstract_factory.py
Intent: 
    Abstract Factory is a creational design pattern that lets you produce
    families of related objects without specifying their concrete classes.

Usage:
    Use the Abstract Factory when your code needs to work with various families 
    of related products, but you don't want it to depend on the concrete classes of those 
    products—they might be unknown beforehand or you simply want to allow for future extensibility.
-------------------------------------------------
"""

from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def render(self) -> str:
        pass


class Checkbox(ABC):

    @abstractmethod
    def render(self) -> str:
        pass


class WindowsButton(Button):

    def render(self) -> str:
        return "Rendering Windows Button"


class WindowsCheckbox(Checkbox):

    def render(self) -> str:
        return "Rendering Windows Checkbox"


class MacOSButton(Button):

    def render(self) -> str:
        return "Rendering MacOS Button"


class MacOSCheckbox(Checkbox):

    def render(self) -> str:
        return "Rendering MacOS Checkbox"


class GUIFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):

    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):

    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


def afactory_create_ui():
    factory = MacOSFactory()
    print("Created Mac AFactory")
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())
