#function is defined using the def keyword, followed by a function name and parentheses:
def my_function():
  print("Hello")
  
  #To call a fuction write its name followed by parentheses
  def my_function():
    print("Hello from a function")

my_function()
my_function()

'''
Functions Names Rules

A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)
'''
#To avoid code repitation we use functions

#functions will return using return statement and itd stop the execution also
def get_greeting():
  return "Hello from a function"
print(get_greeting())

#If a function doesn't have a return statement, it returns None by default.

#Python Function Arguments

#arguments->information can be passed into functions
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

"""
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.
"""
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

#we can assign default values to parameters. If the function is called without an argument, it uses the default value:
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#Keyword Arguments
#we can send arguments with the key = value syntax.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

#keyword arguments, the order of the arguments does not matter.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(name = "Buddy", animal = "dog")

#The phrase Keyword Arguments is often shortened to kwargs in Python documentation.

"""
Positional Arguments:
When you call a function with arguments without using keywords, they are called positional arguments.

Positional arguments must be in the correct order:
"""
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

"""
Mixing Positional and Keyword Arguments:
we can mix positional and keyword arguments in a function call.

However, positional arguments must come before keyword arguments:
"""
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

#we can pass diff datatypes as arguments
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

"""
Positional-Only Arguments:
we can specify that a function can have ONLY positional arguments.

To specify positional-only arguments, add , / after the arguments:
"""
def my_function(name, /):
  print("Hello", name)

my_function("Emil")

"""
Keyword-Only Arguments:
To specify that a function can have only keyword arguments, add *, before the arguments:
"""
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

"""
Combining Positional-Only and Keyword-Only:
You can combine both argument types in the same function.

Arguments before / are positional-only, and arguments after * are keyword-only:
"""
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

"""
*args and **kwargs:

By default, a function must be called with the correct number of arguments.

However, sometimes we may not know how many arguments that will be passed into your function.

*args and **kwargs allow functions to accept a unknown number of arguments.
"""
"""
Arbitrary Arguments - *args:

If we do not know how many arguments will be passed into our function, add a * before the parameter name.

This way, the function will receive a tuple of arguments and can access the items accordingly:
"""
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#The *args parameter allows a function to accept any number of positional arguments.
#Inside the function, args becomes a tuple containing all the passed arguments:
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

#using regular arguments with *args
def my_function(greeting, *names):#regular parameter comes first
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

"""
Arbitrary Keyword Arguments - **kwargs:
If we do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

This way, the function will receive a dictionary of arguments and can access the items accordingly:
"""
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

#we can combine regular arugument with **kwargs but regular parametr as to come first

"""
Combining *args and **kwargs:
You can use both *args and **kwargs in the same function.

The order must be:

regular parameters
*args
**kwargs
"""

#Unpacking Arguments
#The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.

#unpack list wit *
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

#Unpacking Dictionaries with **
#If you have keyword arguments stored in a dictionary, you can use ** to unpack them:
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

"""
SCOPE:
1->Local->accesed locally inside the function
2.->Global->can acces anywhere

if global and local pointing to same variable inside function and outside python will treat that as two diff variable

we can change local variable as global using global keyword
It also change the value of the global variable

nonlocal keyword:
The nonlocal keyword is used to work with variables inside nested functions.
The nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


The LEGB Rule:
Python follows the LEGB rule when looking up variable names, and searches for them in this order:

Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)
"""

"""
Python Decorators:
Decorators let you add extra behavior to a function, without changing the function's code.

A decorator is a function that takes another function as input and returns a new function.
"""

#Basic Decorator
#Define the decorator first, then apply it with @decorator_name above the function.

#A basic decorator that uppercases the return value of the decorated function.
def changecase(func):
    def inner():
        return func().upper()
    return inner  
@changecase
def my_fun():
    return "hello madhan"
print(my_fun())

#Multiple Decorator Calls
#A decorator can be called multiple times. Just place the decorator above the function you want to decorate.
@changecase
def my1_fun():
    return "hlo abin"
print( my1_fun())

#Arguments in the Decorated Function
#Functions that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function:
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

#*args and **kwargs
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

#Decorators can accept their own arguments by adding another wrapper level.
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

"""
Multiple Decorators:
You can use multiple decorators on one function.

This is done by placing the decorator calls on top of each other.

Decorators are called in the reverse order, starting with the one closest to the function.
"""
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

"""
Preserving Function Metadata:
Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

Normally, a function's name can be returned with the __name__ attribute:
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

But, when a function is decorated, the metadata of the original function is lost.

TO fix this Python has a built-in function called "functools.wraps" that can be used to preserve the original function's name and docstring.
we have to import functools

import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)
"""

"""
Generators:
Generators are functions that can pause and resume their execution.

When a generator function is called, it returns a generator object, which is an iterator.

The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.
"""
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)
  
 #Generators allow you to iterate over data without storing the entire dataset in memory.
#Instead of using return, generators use the yield keyword.
#The yield keyword is what makes a function a generator.
#When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off.
def count_up_to(n):
  count = 1
  while count <= n:
    yield count#Unlike return, which terminates the function, yield pauses it and can be called multiple times.


    count += 1

for num in count_up_to(5):
  print(num)
  
""" 
Generators Saves Memory:
Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.

For large datasets, generators save memory: 
"""
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

#You can manually iterate through a generator using the next() function:
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

#When there are no more values to yield, the generator raises a StopIteration exception:
#Generator Expressions:
#->Similar to list comprehensions, you can create generators using generator expressions with parentheses instead of square brackets:

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

#fibnaci seq using genrator
def fin():
  a,b=0,1
  while(True):
    yield a
    a,b=b,a+b
    
gen=fin()
for _ in range(100):
    print(next(gen))
    
#Generators have special methods for advanced control:
#1.The send() method allows you to send a value to the generator:
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")

#2.The close() method stops the generator:
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()

