# python-learniing

check python version by typing `python3 --version` in terminal
ues python3 to run this code 

use python3 
>>> print("Hello, World!")
Hello, World!

indentaion is very important in python
use to space at the begining of a line to define a block of code.


if the following code is run it will throw an error
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
 

 use variables to store values
 like example: -

  x = 5
  y = "hello world"

  print(x)
  print(y)
  
# python commands: -

can be use to explain python code 
comments can be used to make code more readable
comments can be used to prevent execution when testing code.

""" 
this is a multi line comment you can write more than just one line
"""
variables 
python has no command for declaring a variable.

if you want to specify the data type of variable  this can be done with casting .
 exa
 X = str(3)    # x will be '3'

 single or Double quotes are the same
 x = "hello world"
 y = 'hello world'
 
variables are case sensitive
x = 5
X = 6

define variable and rules 

*variables have a short description  or short name

# rules for variable names

1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. Variable names are case-sensitive (age, Age and AGE are three different variables)

# Multi words variable names 
 
Variable names more than one word can be difficult to read.

use camelCase
myVariableName = "John"

pascalCase
MyVariableName = "John"

snake_case
my_variable_name = "John".

# Many Values to Multiple Variables.
 
1.python allows you to assign values to multiple variables in one line.
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# Unpack a Collection :-
 1. if you have a collection of values in a list , tuple etc. 
  2. python allows you to Extract the values into variables.
   3. is called unpacking.

# Example :-
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output variables

in the print() function you can output multiple variables,
separated by a comma:

# Example :-
x = 5
y = "John"
print(x, y)

# The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

1. Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

2. Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

3. Complex numbers are written with a "j" as the imaginary part:

# Python Casting
 # Specify a Variable Type

There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals


#  String: -

1. Strings in python are surrounded by either single quotation marks, or double quotation marks.

(ex)  'hello' is the same as "hello".


  # multiple Sring: 
   1. You can assign a multiline string to a variable by using three quotes:

# Strings are Arrays
