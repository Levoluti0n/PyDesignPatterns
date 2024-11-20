"""
-------------------------------------------------
File: singleton.py
Intent: 
    Singleton is a creational design pattern that lets you ensure that a class 
    has only one instance, while providing a global access point to this instance.
    
Usage:
    Use the Singleton pattern when a class in your program should have just a single instance 
    available to all clients; for example, a single database object shared by different parts of the program.
-------------------------------------------------
"""

'''
    *** Race Condition
'''
# import threading

# class Singleton: 
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance == None:
#             cls._instance = super(Singleton, cls).__new__(cls)
#             return cls._instance

# def create_singleton():
#     obj = Singleton()
#     print(f"Instance ID: {id(obj)}")

# threads = [threading.Thread(target=create_singleton) for _ in range(10)]
# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join()

'''
   *** Solution of Race Condition
'''

import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    pass

def create_singleton():
    obj = Singleton()
    print(f"Instance ID: {id(obj)}")

def threads_test():
    threads = [threading.Thread(target=create_singleton) for _ in range(10)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()