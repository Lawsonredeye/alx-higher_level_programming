# Python Inheritance

As much as this sounds like inheriting a property from someone well when it comes to python classes can actually inherit another classes properties at any moment. 

Now you may be wondering, **“How is that even Possible?”** Well, in the amazing world of Python classes can actually have access to already existing classes **A.K.A Parent classes**, to get methods from as well as instances too.

This is very useful when it comes to code reusability as well as other features that would help you in the programming community.

## How to create inheritance class / class that inherits from another class?

well this is fairly simple, all you need is a Base Class and a Sub Class. 

**Base classes** are also known as Parent classes that are passed as a value to a subclass( A.K.A Child classes) as an object or as an argument. 

Syntax:

`class Child_Class_name(Parent_Class_Name):`

`class Car` - Parent Class

`class Bugatti(Car)` - Child class inheriting from the Parent class Car

## Magic Methods

classes uses magic methods as well as inheritance and they are listed below.

**super().__init__()**: this gives your child class the ability to be able to have access to the same initialization that the parent class has as well as the ability to tweak what was present there.

**`class`** `Person():`

`**def**` `__init__(self, name, age):`

`self.name **=**` `name`

`self.age **=**` `age`

`**def**` `display(self):`

`print(self.name, self.age)`

`# child class`

**`class`** `Student(Person):`

`**def**` `__init__(self, name, age):`

`self.sName **=**` `name`

`self.sAge **=**` `age`

`# inheriting the properties of parent class`

`super().__init__("Lawson", age)`

`**def**` `displayInfo(self):`

`**print**(self.sName, self.sAge)`

`obj **=**` `Student("kelvin", 45)`

`obj.display()`

`obj.displayInfo()`