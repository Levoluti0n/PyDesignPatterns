"""
-------------------------------------------------
File: decorator.py
Intent: 
    Decorator is a structural design pattern that lets you
    attach new behaviors to objects by placing these objects
    inside special wrapper objects that contain the behaviors.

Usage:
    Use the Decorator pattern when you need to be able to assign
    extra behaviors to objects at runtime without breaking the code that uses these objects.
-------------------------------------------------
"""

from abc import ABC, abstractmethod
import zlib
import base64

class DataSource(ABC):
    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def read_data(self):
        pass

class InMemoryDataSource(DataSource):
    def __init__(self):
        self._data = None

    def write_data(self, data):
        self._data = data
        print(f"Data stored: {data}")

    def read_data(self):
        print(f"Data retrieved: {self._data}")
        return self._data
    
class DataSourceDecorator(DataSource):
    def __init__(self, wrappee: DataSource):
        self._wrappee = wrappee

    def write_data(self, data):
        self._wrappee.write_data(data)

    def read_data(self):
        return self._wrappee.read_data()
    
class CompressionDecorator(DataSourceDecorator):
    def write_data(self, data):
        compressed_data = base64.b64encode(zlib.compress(data.encode()))
        print("Data compressed.")
        super().write_data(compressed_data.decode())

    def read_data(self):
        data = super().read_data()
        decompressed_data = zlib.decompress(base64.b64decode(data)).decode()
        print("Data decompressed.")
        return decompressed_data

class EncryptionDecorator(DataSourceDecorator):
    def write_data(self, data):
        encrypted_data = base64.b64encode(data.encode())
        print(f"Data encrypted")
        super().write_data(encrypted_data.decode())

    def read_data(self):
        data = super().read_data()
        decrypted_data = base64.b64decode(data).decode()
        print("Data decrypted.")
        return decrypted_data
    
def decorator_crypting():
    in_memory_source = InMemoryDataSource()
    compressed_encrypted_source = CompressionDecorator(EncryptionDecorator(in_memory_source))

    data_to_store = "This is some secret data!"
    print("\nWriting Data...")
    compressed_encrypted_source.write_data(data_to_store)

    print("\nReading Data...")
    restored_data = compressed_encrypted_source.read_data()
    print(f"\nRestored Data: {restored_data}")