"""
-------------------------------------------------
File: flyweight.py
Intent:
    Flyweight is a structural design pattern that lets you fit more
    objects into the available amount of RAM by sharing common parts of
    state between multiple objects instead of keeping all of the data in each object.

Usage:
    Use the Flyweight pattern only when your program must
    support a huge number of objects which barely fit into available RAM.
-------------------------------------------------
"""

from abc import ABC, abstractmethod


class TreeType:

    def __init__(self, species, texture, color):
        self.species = species
        self.texture = texture
        self.color = color

    def display(self, x, y):
        print(
            f"TreeType: {self.species}, Texture: {self.texture}, Color: {self.color}, Position: ({x}, {y})"
        )


class TreeTypeFactory:

    def __init__(self):
        self._tree_types = {}

    def get_tree_type(self, species, texture, color):
        key = (species, texture, color)
        if key not in self._tree_types:
            self._tree_types[key] = TreeType(species, texture, color)
            print(f"Created new TreeType: {key}")
        else:
            print(f"Reusing existing TreeType: {key}")
        return self._tree_types[key]


class Tree:

    def __init__(self, x, y, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def display(self):
        self.tree_type.display(self.x, self.y)


def flyweight_forest_draw():
    factory = TreeTypeFactory()
    tree1 = Tree(1, 2, factory.get_tree_type("Oak", "Bark", "Green"))
    tree2 = Tree(2, 3, factory.get_tree_type("Pine", "Bark", "Green"))
    tree3 = Tree(5, 8, factory.get_tree_type("Oak", "Needle", "Green"))
    tree1.display()
    tree2.display()
    tree3.display()
    print(f"{''*5}Total TreeTypes created: {len(factory._tree_types)}")
