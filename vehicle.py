from abc import ABC, abstractmethod
# abc module in python ==> 'Abstract Base Classes': it provides the insfracture for defining abstract base classes (ABC), which can be used to define interfaces when other classes must implement specific methods. The 'abc' module includes the 'ABC' class and the 'abstractmethod' decorator, which are used to create abstract base classes and abstract methods, respectively.

# 'ABC' Class: This is a base class for defining abstract base classes. Classes that inherit properties from 'ABC' are considered abtract base classes. It is a subclass of 'object'

# 'abstract method' Decorator: This decorator is used to declare methods as abstract.
# Why Use Abstract Base Classes?

# Enforce Method Implementation: Ensure that subclasses provide implementations for all abstract methods.
# Code Readability: Clearly define a common interface for a group of related classes.
# Type Checking: Enable better type checking and code analysis tools to understand the intended interface.
# Summary
# abc is a module in Python for defining abstract base classes.
# ABC is a class from the abc module used to create abstract base classes.
# abstractmethod is a decorator used to declare abstract methods that must be implemented by subclasses.
# Using abstract base classes helps to create a clear and enforceable contract for the methods that subclasses must implement, enhancing code reliability and maintainability.

class Vehicle(ABC):
    @abstractmethod

    def start_engine(self):
        pass