"""
-------------------------------------------------
File: command.py
Intent: 
    Command is a behavioral design pattern that turns a request
    into a stand-alone object that contains all information about the request.

Usage:
    Use the Command pattern when you want to parametrize objects with operations.

-------------------------------------------------
"""

from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Light:

    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")


class Fan:

    def start(self):
        print("Fan is RUNNING")

    def stop(self):
        print("Fan is STOPPED")


class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class FanStartCommand(Command):

    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.start()

    def undo(self):
        self.fan.stop()


class FanStopCommand(Command):

    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.stop()

    def undo(self):
        self.fan.start()


class SmartHomeController:

    def __init__(self):
        self.command_history = []
        self.redo_stack = []

    def execute_command(self, command):
        command.execute()
        self.command_history.append(command)
        self.redo_stack.clear()

    def undo(self):
        if self.command_history:
            command = self.command_history.pop()
            command.undo()
            self.redo_stack.append(command)
        else:
            print("Nothing to undo")

    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.command_history.append(command)
        else:
            print("Nothing to redo")


def command_smart_home():
    light = Light()
    fan = Fan()
    light_on = LightOnCommand(light)
    fan_start = FanStartCommand(fan)

    controller = SmartHomeController()

    controller.execute_command(light_on)
    controller.execute_command(fan_start)

    controller.undo()
    controller.undo()

    controller.redo()
