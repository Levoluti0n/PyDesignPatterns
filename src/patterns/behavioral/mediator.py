"""
-------------------------------------------------
File: mediator.py
Intent: 
    Mediator is a behavioral design pattern that lets you reduce
    chaotic dependencies between objects. The pattern restricts direct
    communications between the objects and forces them to collaborate only via a mediator object.

Usage:
    Use the Mediator pattern when it's hard to change some
    of the classes because they are tightly coupled to a bunch of other classes.
-------------------------------------------------
"""

from abc import ABC, abstractmethod


class Mediator(ABC):

    @abstractmethod
    def register(self, user):
        pass

    @abstractmethod
    def send(self, sender_name, receiver_name, message):
        pass

    @abstractmethod
    def broadcast(self, sender_name, message):
        pass


class Colleague(ABC):

    def __init__(self, name):
        self.name = name
        self.mediator = None

    @abstractmethod
    def send(self, receiver_name, message):
        pass

    @abstractmethod
    def broadcast(self, message):
        pass

    @abstractmethod
    def receive(self, sender_name, message):
        pass


class ChatRoom(Mediator):

    def __init__(self) -> None:
        self.participants = {}

    def register(self, user):
        self.participants[user.name] = user
        user.mediator = self
        print(f"{user.name} joined the chat room.")

    def send(self, sender_name, receiver_name, message):
        receiver = self.participants.get(receiver_name)
        if receiver:
            receiver.receive(sender_name, message)
        else:
            print(
                f"Message from {sender_name} to {receiver_name} failed: User not found."
            )

    def broadcast(self, sender_name, message):
        for name, user in self.participants.items():
            if name != sender_name:
                user.receive(sender_name, message)


class User(Colleague):

    def send(self, receiver_name, message):
        if self.mediator:
            print(f"{self.name} to {receiver_name}: {message}")
            self.mediator.send(self.name, receiver_name, message)
        else:
            print(f"{self.name} is not part of a chat room.")

    def broadcast(self, message):
        if self.mediator:
            print(f"{self.name} (broadcast): {message}")
            self.mediator.broadcast(self.name, message)
        else:
            print(f"{self.name} is not part of a chat room.")

    def receive(self, sender_name, message):
        print(f"{self.name} received from {sender_name}: {message}")


def mediate_chat():
    chatroom = ChatRoom()
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    chatroom.register(alice)
    chatroom.register(bob)
    chatroom.register(charlie)

    alice.send("Bob", "Hi Bob!")
    bob.send("Alice", "Hey Alice, how are you?")
    charlie.broadcast("Hello everyone!")
