"""
-------------------------------------------------
File: bridge.py
Intent: 
    Composite is a structural design pattern that lets
    you compose objects into tree structures and then work
    with these structures as if they were individual objects.

Usage:
    Use the Composite pattern when you have
    to implement a tree-like object structure.
-------------------------------------------------
"""

from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self, indent=0):
        pass

    @abstractmethod
    def size(self):
        pass

class File(FileSystemComponent):
    def __init__(self, name, file_size):
        super().__init__(name)
        self._file_size = file_size

    def display(self, indent=0):
        print(f"{' ' * indent}- File: {self.name} ({self._file_size} KB)")

    def size(self):
        return self._file_size

class Folder(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self._children = []

    def add(self, component: FileSystemComponent):
        self._children.append(component)

    def remove(self, component: FileSystemComponent):
        self._children.remove(component)

    def display(self, indent=0):
        print(f"{' ' * indent}+ Folder: {self.name}")
        for child in self._children:
            child.display(indent + 2)

    def size(self):
        return sum(child.size() for child in self._children)

def composite_folder():
    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 200)
    file3 = File("file3.jpg", 500)

    folder1 = Folder("Documents")
    folder1.add(file1)
    folder1.add(file2)

    folder2 = Folder("Pictures")
    folder2.add(file3)

    root = Folder("Root")
    root.add(folder1)
    root.add(folder2)

    print("Filesystem Structure:")
    root.display()

    print(f"\nTotal Size: {root.size()} KB")
