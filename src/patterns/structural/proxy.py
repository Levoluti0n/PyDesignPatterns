"""
-------------------------------------------------
File: flyweight.py
Intent:
    Proxy is a structural design pattern that lets you provide a
    substitute or placeholder for another object. A proxy controls
    access to the original object, allowing you to perform something 
    either before or after the request gets through to the original object.

Usage:
    Logging requests (logging proxy)
    Access control (protection proxy)
    Lazy initialization (virtual proxy)
    Caching request results (caching proxy)
    Local execution of a remote service (remote proxy)
-------------------------------------------------
"""

from abc import ABC, abstractmethod

class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")

class ImageProxy(ABC):
    @abstractmethod
    def display(self):
        pass

class VirtualImageProxy(ImageProxy):
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def display(self):
        if not self._real_image:
            self._real_image = RealImage(self.filename)
        self._real_image.display()

class User(ABC):
    @abstractmethod
    def has_access(self):
        pass

class AdminUser(User):
    def has_access(self):
        return True

class RegularUser(User):
    def has_access(self):
        return False
    
class RestrictedImage(ABC):
    @abstractmethod
    def display(self):
        pass

class ProtectionProxyImage(RestrictedImage):
    def __init__(self, filename, user: User):
        self.filename = filename
        self.user = user
        self._real_image = RealImage(filename)

    def display(self):
        if self.user.has_access():
            self._real_image.display()
        else:
            print(f"Access denied: {self.user.__class__.__name__} cannot access {self.filename}")

def proxy_image():
    print("Using Virtual Proxy:")
    proxy1 = VirtualImageProxy("image1.jpg")
    proxy1.display()
    proxy1.display()

    print("\nUsing Protection Proxy:")
    admin_user = AdminUser()
    regular_user = RegularUser()

    protected_image = ProtectionProxyImage("restricted_image.jpg", admin_user)
    protected_image.display()

    protected_image = ProtectionProxyImage("restricted_image.jpg", regular_user)
    protected_image.display()

    