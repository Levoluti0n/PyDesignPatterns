"""
-------------------------------------------------
File: iterator.py
Intent: 
    Iterator is a behavioral design pattern that
    lets you traverse elements of a collection without
    exposing its underlying representation (list, stack, tree, etc.).

Usage:
    Use the Iterator pattern when your collection has
    a complex data structure under the hood, but you want
    to hide its complexity from clients (either for convenience or security reasons).
-------------------------------------------------
"""


class DatasetIterator:

    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]


class Dataset:

    def __init__(self, records):
        self.records = records

    def __iter__(self):
        return DatasetIterator(self.records)


def iter_data():
    data = Dataset([1, 2, 3, 4, 5, 6, 7, 8, 9])

    res = []
    for item in data:
        res.append(item)
    print(*res, sep=" -> ")
