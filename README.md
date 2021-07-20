Python OOP, Interfaces

Inheritance
Python also has a super() function that will make the child class inherit all the methods and properties from its parent

Interface Overview
At a high level, an interface acts as a blueprint for designing classes. They define abstract methods.

An abstract method is one that the interface simply defines and does not
implement. 

Classes then implement the interface and give concrete meaning to the interface’s abstract methods.

Python does not have an interface keyword as languages like C++, Java, Go do.

Python doesn’t require the class that’s implementing the interface to define all of the interface’s abstract methods.

Informal Interfaces
Python’s dynamic nature allows you to implement an informal interface. 

An informal Python interface is a class that defines methods that can be overridden, but there’s no strict enforcement.

Informal Interface looks identical to a standard python class, so you rely on duck typing to inform users that this is an interface and should be used accordingly. 

 You can view a class’s MRO(method resolution order) by using the dunder method cls.__mro__
Such informal interfaces are fine for small projects.

Using Metaclasses
We want issubclass(EmlParser, InformalParserInterface) to return False when the implementing class doesn’t define all of the interface’s abstract methods.
To do this, you’ll create a metaclass called ParserMeta. You’ll be overriding two dunder methods:
.__instancecheck__()
.__subclasscheck__()
By using a metaclass, you don’t need to explicitly define the subclasses. Instead, the subclass must define the required methods.
As you can see, UpdatedInformalParserInterface is a superclass of PdfParserNew, but it doesn’t appear in the MRO.
This unusual behavior is caused by the fact that UpdatedInformalParserInterface is a virtual base class of PdfParserNew.
Virtual Base Class
The key difference between these and standard subclasses is that virtual base classes use the .__subclasscheck__() dunder method to implicitly check if a class is a virtual subclass of the superclass. Additionally, virtual base classes don’t appear in the subclass MRO
 
Formal Interfaces

In order to create a formal Python interface, you’ll need a few more tools from Python’s abc module.
Rather than create your own metaclass, you’ll 
 you’ll use abc.ABCMeta as the metaclass. 
Then, you’ll overwrite .__subclasshook__() in place of .__instancecheck__() and .__subclasscheck__(), as it creates a more reliable implementation of these dunder methods.
Using abc to Register a Virtual Subclass
Once you’ve imported the abc module, you can directly register a virtual subclass by using the .register() metamethod.
class Double(metaclass=abc.ABCMeta):
    """Double precision floating point number."""
    pass

Double.register(float)


By using the .register() meta method, you’ve successfully registered Double as a virtual subclass of float.
Once you’ve registered Double, you can use it as class decorator to set the decorated class as a virtual subclass:

@Double.register
class Double64:
    """A 64-bit double-precision floating-point number."""
    pass

print(issubclass(Double64, Double))  # True

The decorator register method helps you to create a hierarchy of custom virtual class inheritance.

Using Subclass Detection With Registration

You must be careful when you’re combining .__subclasshook__() with .register(), as .__subclasshook__() takes precedence over virtual subclass registration.

To ensure that the registered virtual subclasses are taken into consideration, you must add NotImplemented to the .__subclasshook__() dunder method.

Using Abstract Method Declaration

An abstract method is a method that’s declared by the Python interface, but it may not have a useful implementation. The abstract method must be overridden by the concrete class that implements the interface in question.

To create abstract methods in Python, you add the @abc.abstractmethod decorator to the interface’s methods. In the next example, you update the FormalParserInterface to include the abstract methods .load_data_source() and .extract_text():


Links
https://realpython.com/python-interface/#python-interface-overview

