"""
-------------------------------------------------
File: bridge.py
Intent: 
    Bridge is a structural design pattern that lets you split
    a large class or a set of closely related classes into two
    separate hierarchies—abstraction and implementation—which
    can be developed independently of each other.

Usage:
    Use the Bridge pattern when you want to divide
    and organize a monolithic class that has several
    variants of some functionality (for example,
    if the class can work with various database servers).
-------------------------------------------------
"""

from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def power(self):
        pass

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

    @abstractmethod
    def is_on(self):
        pass

class TV(Device):
    def __init__(self):
        self._is_on = False
        self._volume = 10

    def power(self):
        self._is_on = not self._is_on
        print("\t +TV turned ON" if self._is_on else "TV turned OFF")

    def volume_up(self):
        if self._is_on:
            self._volume += 1
            print(f"\t +TV Volume: {self._volume}")

    def volume_down(self):
        if self._is_on:
            self._volume -= 1
            print(f"\t +TV Volume: {self._volume}")

    def is_on(self):
        return self._is_on

class Radio(Device):
    def __init__(self):
        self._is_on = False
        self._volume = 5

    def power(self):
        self._is_on = not self._is_on
        print("\t +Radio turned ON" if self._is_on else "Radio turned OFF")

    def volume_up(self):
        if self._is_on:
            self._volume += 1
            print(f"\t +Radio Volume: {self._volume}")

    def volume_down(self):
        if self._is_on:
            self._volume -= 1
            print(f"\t +Radio Volume: {self._volume}")

    def is_on(self):
        return self._is_on

class Remote(ABC):
    def __init__(self, device: Device):
        self.device = device

    @abstractmethod
    def toggle_power(self):
        pass

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

class BasicRemote(Remote):
    def toggle_power(self):
        print("Basic Remote: Toggling Power")
        self.device.power()

    def volume_up(self):
        print("Basic Remote: Increasing Volume")
        self.device.volume_up()

    def volume_down(self):
        print("Basic Remote: Decreasing Volume")
        self.device.volume_down()

class AdvancedRemote(Remote):
    def toggle_power(self):
        print("Advanced Remote: Toggling Power")
        self.device.power()

    def volume_up(self):
        print("Advanced Remote: Increasing Volume")
        self.device.volume_up()

    def volume_down(self):
        print("Advanced Remote: Decreasing Volume")
        self.device.volume_down()

    def mute(self):
        print("Advanced Remote: Muting Device")
        if self.device.is_on():
            print("Device muted (volume set to 0)")

def bridge_toggle():
    tv = TV()
    print("Created TV for Remote Controller")
    advanced_remote = AdvancedRemote(tv)
    advanced_remote.toggle_power()
    advanced_remote.volume_up()
    advanced_remote.mute()
    advanced_remote.toggle_power()