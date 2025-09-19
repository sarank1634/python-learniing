# Global Variables
  #1. Variables that are created outside of a function .
  #2. Global variables can be used by everyone , both inside of functions and outside.

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

x = "awesome"

def myfun():
  x = "fantastic"
  print("Python is " + x)

myfun()

print("Python is " + x)