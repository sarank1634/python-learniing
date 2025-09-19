# ike many other popular programming languages, strings in Python are arrays of unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1])

# using for loop
for x in "banana":
    print(x)

# length of string:
a = "hello world "
print(len(a))

# Check String
# To check if aTo check if a certain phrase or character is present in a string, we can use the keyword in.
#certain phrase or character is present in a string, we can use the keyword in.

txt = "hi hello world"
print("world" in txt)

txt = "the best thing in life are free!"
if "free" in txt:
    print("Yes, `free' is presented.")


# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "the best things in life are free!"
print("epensive" not in txt)