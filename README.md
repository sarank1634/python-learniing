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
