### Python Magic Methods. Hi there!
> Here you can see just a bit about `python magic methods`. This is my small documentation, yay :) 

### `__init__`
It's initialization, which performed for every new class instance. With this method we can execute a part of code in the initialization moment and define different parameters for our instance, for example.
```
def __init__(self, argument1, argument2, ...):
    self.argument1 = argument1
    self.argument2 = argument2
    self.argument3 = really_important_func(self.argument1, self.argument2)
    ...
```
### `__str__`
Method, which can help us to redefine instance output in console. For example, imagine that we have many instances of class and every instance is a planet. Let the name of the planet be displayed in the console:
```
def __str__(self):
    return self.name 
```
### `__self__ , __repr__`
`__self__` refers to the external representation of an instance of a class <br>
`__repr__` refers to the internal representation that Python itself will handle:
```
def __repr__(self):
    return f"Planet {self.name}"
```
### `__dict__`
Allows you to see all the attributes of the class and instance
```
class.__dict__
>>> all class methods 

instance.__dict__
>>> all instance atributes
```
### `__doc__`
Let you see documentation for func, class etc.
```
def really_important_func(a, b):
    """doc string"""
    pass

really_important_func.__doc__
>>> doc string
```

### `__class__`
Allows you to see which file a lot of structural project belongs to

### `__new__`
Class instance constructor:
```
def __new__(cls, *args, **kwargs)
    obj = super().__new__(cls) # creating a new instance of the class
    return obj
```
### `__getattr__`, `__getattribute__`
Checks if an instance of a class has an attribute.
```
def __getattr__(self, name):
    return message # if atribute not found
```
```
def __getattribute__(self, name):
    return message # will always return a message
```
### `__setattr__`, `__delattr__`
`__settattr__(self, name, value):` controlls the behavior when we set attribute
`__delattr__(self, name):` controlls the behavior when we delete attribute
### `__call__`
`__call__(self, func):` defines behavior when a class is called.
Using `__call__`, you can define a logger, which can then be used as a decorator.
```
class Logger:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, func):
        with open(self.filename, 'w') as file:
	    fil.write('Logging Message')
	return func

logger = Logger('log.txt')

@logger
def somethink_func():
    pass
```
### `__add__` etc.
Override the additional, substraction, multiplication behavior of instances etc.

### `__getitem__, __setitem__`
`__getitem__` defnes the behavior of an object when accessed by index or key - `obj[key]` <br>
`__setitem__` defines the behavior of an object when assigned by index or key - `obj[key]=value`

### `__slots__`
Allows you to rigidly set the number of arguments and their names:
```
__slots__ = ['arg1', 'arg2',...]
```

Actually it isn't all methods, here you can see just a bit. Here I publish only my personal experience. All methods with their description you can find on dock.python.org

---

### Find me here:
* [Telegram](https://t.me/grnbows) </br>
* [Вконтакте](https://vk.com/grnbows) </br>
* [Instagram](https://www.instagram.com/grnbows) </br>
* [Twitter](https://twitter.com/grnbows) </br>

<i>With respect and love,</i></br> by grnbows
