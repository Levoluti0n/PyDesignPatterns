"""
-------------------------------------------------
File: chain_of_responsibility.py
Intent: 
    Chain of Responsibility is a behavioral design pattern that lets
    you pass requests along a chain of handlers. Upon receiving a request,
    each handler decides either to process the request or to pass it to the next handler in the chain.

Usage:
    Use the Chain of Responsibility pattern when your
    program is expected to process different kinds of requests
    in various ways, but the exact types of requests and their sequences are unknown beforehand.
-------------------------------------------------
"""

from abc import ABC, abstractmethod


class Handler(ABC):

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)


class DebugLogger(Handler):

    def handle(self, request):
        level, message = request
        if level == "DEBUG":
            print(f"[DEBUG]: {message}")
        elif self.next_handler:
            self.next_handler.handle(request)


class InfoLogger(Handler):

    def handle(self, request):
        level, message = request
        if level == "INFO":
            print(f"[INFO]: {message}")
        elif self.next_handler:
            self.next_handler.handle(request)


class DefaultLogger(Handler):

    def handle(self, request):
        level, message = request
        print(f"[DEFAULT]: {level} - {message}")


def chain_requests():
    debug_logger = DebugLogger()
    info_logger = InfoLogger()
    default_logger = DefaultLogger()

    debug_logger.set_next(info_logger).set_next(default_logger)
    requests = [("DEBUG", "This is a debug message."),
                ("INFO", "This is an informational message."),
                ("WARNING", "This is an unhandled warning message.")]

    for req in requests:
        debug_logger.handle(req)
