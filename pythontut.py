import sys
import math
import random
import threading
import time
import re # need this for regex

from functools import reduce

print("Hello World!")
name = input("What is your name: ")
print("Hi", name)

# Single line comment

''' 
multiple-line comments
'''
# Generally recommended to use multiple single line comments instead
# Basic Data Types: int, float, complex, strings, bool

print(type(10))  # returns the data type

f1 = 1.1111111111  # floats accurate up to 15 decimals like most languages
complexNum = 1 + 2j  # complex number, yes this just works
b1 = True  # booleans, true or false
string1 = "This is a string"  # Escape sequences - \' \" \t \\ \n
string2 = '''Triple quotes - can use " or ' without causing errors '''

# You can cast to different types with int, float, str, chr
print("Cast ", type(int(5.4)))  # to int
print("Cast 2 ", type(str(5.4)))  # to string
print("Cast 3 ", type(chr(97)))  # to string
print("Cast 4 ", type(ord('a')))  # to int

print(19, 5, 1997, sep='/')  # Python doesn't like leading zeros.
# Use "%02d" % 5 to output 05.
print("No new line", end='')  # print automatically adds a new line.

# string formatting example
print("\n%04d %s %.2f %c" % (1, "Abhishek", 1.11111, 'A'))

# --------------- Math Functions
print("5 + 2 =", 5 + 2)  # add
print("5 - 2 =", 5 - 2)  # subtract
print("5 * 2 =", 5 * 2)  # multiplyply
print("5 / 2 =", 5 / 2)  # divide
print("5 % 2 =", 5 % 2)  # modulus
print("5 ** 2 =", 5 ** 2)  # powers
print("5 // 2 =", 5 // 2)  # integer divide, disregards remainder

# Operator precedence - Parenthesis > Power > Multiplication > Addition > Left to right

int1 = 1
int1 += 1  # '+=' takes variable and adds 1 to it

print("abs(-1) ", abs(-1))  # absolute
print("max(5, 4) ", max(5, 4))  # max
print("min(5, 4) ", min(5, 4))  # min
print("pow(2, 2) ", pow(2, 2))  # power
print("ceil(4.5) ", math.ceil(4.5))  # returns smallest int greater than 4.5
print("floor(4.5) ", math.floor(4.5))  # returns largest int less than 4.5
print("round(4.5) ", round(4.5))  # rounds number
print("exp(1) ", math.exp(1))  # e**x
print("log(e) ", math.log(math.exp(1)))
print("log(100) ", math.log(100, 10))  # Base 10 Log
print("sqrt(100) ", math.sqrt(100))
print("sin(0) ", math.sin(0))
print("cos(0) ", math.cos(0))
print("tan(0) ", math.tan(0))
print("asin(0) ", math.asin(0))
print("acos(0) ", math.acos(0))
print("atan(0) ", math.atan(0))
print("sinh(0) ", math.sinh(0))
print("cosh(0) ", math.cosh(0))
print("tanh(0) ", math.tanh(0))
print("asinh(0) ", math.asinh(0))
print("acosh(pi) ", math.acosh(math.pi))
print("atanh(0) ", math.atanh(0))
print("hypot(0) ", math.hypot(10, 10))  # sqrt(x*x + y*y)
print("radians(0) ", math.radians(0))  # converts deg to rad
print("degrees(pi) ", math.degrees(math.pi))  # converts rad to deg

print("Random", random.randint(1, 100))  # random num between 1 and 100

print(math.inf - math.inf)  # returns NaN, Not a Number

# -------------- Conditionals
# Comparison Operators : < > <= >= == !=
# Logical operators and, or, not

number = int(input("Enter a number: "))
if number >= 10:
    print("10 or above")
elif number <= 5:
    print("5 or less")
else:
    print("between 5 and 10")

# Ternary operator in Python
# condition_true if condition else condition_false
age = 30
canVote = True if age >= 18 else False

# ---------- Strings

print(r"I'll be ignored \n")  # Raw strings ignore escape sequences
print("Hello " + "You")  # Combine strings with +
str3 = "Hello You"
print("Length ", len(str3))  # Get string length
print("1st ", str3[0])  # Character at index
print("Last ", str3[-1])  # Last character
print("1st 3 ", str3[0:3])  # 1st 3 chrs. Start, up to not including
# Get every other character, last is a step
print("Every Other ", str3[0:-1:2])

# You can't change an index value like this
# str3[0] = "a" because strings are immutable
# (Can't Change)
# You could do this
str3 = str3.replace("Hello", "Goodbye")
print(str3)


str3 = str3[:8] + "y" + str3[9:]
print(str3)  # You could also slice front and back and replace what you want to change

print("you" in str3)  # Test if string in string
print("you" not in str3)  # Test if not in

print("You Index ", str3.find("you"))  # Find first index for match or -1

# Trim white space from right and left, also lstrip and rstrip
print("    Hello    ".strip())

# Convert a list into a string and separate with spaces
print(" ".join(["Some", "Words"]))

# Convert string into a list with a defined separator or delimiter
print("A, string".split(", "))

# Formatted output with f-string
int1 = int2 = 5
print(f'{int1} + {int2} = {int1 + int2}')

print("A String".lower())  # To lower case
print("A String".upper())  # To upper case
print("abc123".isalnum())  # Is letter or number
print("abc".isalpha())  # Is characters
print("abc".isdigit())  # Is numbers

# ---------- List

l1 = [1, 3.14, "String Cheese", True]
print("Length", len(l1))
print("1st item", l1[0])
print("Last item", l1[-1])

l1[0] = 2
l1[2:4] = [37, False]  # From 2 to 4, not including 4. Change multiplyple values
l1[2:2] = [4, 5, 6, 7]  # Insert values at 2 without deleting
l1.insert(2, "Entered at index 2")  # Alternative to inserting at an index
l2 = l1 + ["l2 list 1", "l2 list 2"]  # Add lists.
print("l2", l2)

l2 = ["beginning of list", 21] + l1  # Beginning of list
l2.remove(2)  # Remove a value
l2.append(object)
l2.pop(0)  # Remove item at index 0
l3 = [[2, 3], [4, 5]]  # multi-dimensional lists
print("print: ", l3[1][1])  # Print index 1, index 1
print("Does 2 exists", 2 in l1)
print("Min ", min([1, 2, 3]))  # print min or max of a list
print("Max ", max([1, 2, 3]))
print("1st 2", l1[0:2])  # list manipulation
print("Every Other ", l1[0:-1:2])
print("Reverse ", l1[::-1])

# ---------- Loop

# While loop. Execute something as long as condition is true.
w1 = 1  # Condition
while w1 < 5:
    print(w1)
    w1 += 1

w2 = 0
while w2 <= 20:
    if w2 % 4 == 0:
        print(w2)
    elif w2 == 11:
        break  # Loop terminates
    else:
        w2 += 1
        continue  # Skips rest of the code, continues with next loop iteration
    w2 += 1

l4 = [1, 3.14, 4, 5, 6]
while len(l4):  # This code cycles through a list
    print(l4.pop(0))  # Destructive, destroys the list

# For loops: Perform an action X number of times
# range(0, 10) performs actions from 0-9, so 10 times
# end="" eliminates new line
for x in range(0, 10):
    print(x, ' ', end="")
print()

for x in [2, 4, 6, 8]:
    print(x)  # Cycles through a list without destroying it

# ---------- Iterator
l5 = [3, 6, 9]
itr = iter(l5)  # returns an iterator
print(next(itr))  # Grab next value
print(next(itr))

# ---------- Ranges

print(list(range(0, 10, 2)))  # 0 to 10 in steps of 2

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

# ---------- Tuples
# Lists, but they can't be changed

t1 = (1, 3.14, "Abhishek")

# Everything that works with lists works with tuples as long as you don't try to change stuff.

# Why use tuples then? More efficient behind the scenes, less memory use and performance impact.

# ---------- Dictionaries
# Lists of pairs. Can use any data types.
heroes = {
    "Spider-Man": "Peter Parker",
    "Captain America": "Steve Rodgers",
    "Thor": "Thor"
}

villains = dict([
    ("Loki", "Loki"),
    ("Winter Soldier", "Bucky Barnes")
])

sv = sorted(villains.items()) # takes a sequence and sorts it in ascending order


print("Length", len(heroes))
print(heroes["Spider-Man"])
heroes["Iron Man"] = "Tony Stark"  # Add or change values
print(list(heroes.items()))  # Returns a list of tuples
print(list(heroes.keys()))  # Returns just the keys
print(list(heroes.values()))  # Just values

del heroes["Iron Man"]  # Remove item without returning it
print(heroes.pop("Captain America"))  # Return then remove
print("Spider-Man" in heroes)  # Returns a boolean

for k in heroes:
    print(k)

for j in heroes.values():
    print(j)

dic1 = {"item": "Bread", "price": 1.20}
print("%(name)s costs $%(price).2f" % dic1)

# ---------- Sets
# Sets are lists that are unordered, unique
# Once a set is created, you cannot change its items, but you can add new items.

s1 = set(["Abhishek", 1])
s2 = {"Abs", 2}

s3 = s1 | s2  # Join sets
s3.add("Extra item")
s3.discard("Extra item")
print("Random", s3.pop())  # Remove random value
s3 |= s2  # Add values
print(s1.intersection(s2))  # Return common values, can use multiple sets
print(s1.symmetric_difference(s2))  # Returns unique values that aren't common
print(s1.difference(s2))  # Values in s1 but not s2
s3.clear()

s4 = frozenset([1, 2, 3])  # Set that can't be edited

# ---------- Functions
# Use functions for code reuse, organisation


def get_sum(num1: int, num2=1): # use def to name/define the function
    return num1 + num2


print(get_sum(4, 5))


def get_sum2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(get_sum2(0, 10, 1))


def next_2(num):
    return num + 1, num + 2  # Return multiple values


i1, i2 = next_2(7)
print(i1, i2)


def multiply_by(num):
    return lambda x: x * num  # lambda is used to create an unnamed function


print("2 x 2 = ", multiply_by(2)(2))


def multiply_list(list, func):  # Pass a function to another function
    for x in list:
        print(func(x))


multiply_by_4 = multiply_by(4)
multiply_list(list(range(0, 4, 1)), multiply_by_4)

power_list = [lambda x: x ** 2, lambda x: x ** 3]  # List of functions

# ---------- Map
# Used to apply a function on a list
one_to_four = range(1, 5, 1)


def times2(x): return x*2


print(list(map(times2, one_to_four)))

# ---------- Filter
# Filters items based on a function
# This line of code prints even values from a list
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

# ---------- Reduce
# Reduce takes a list and returns a single result
print(reduce((lambda x, y: x + y), range(1, 6)))

# ---------- Exceptions
# Used to handle errors that would otherwise crash your program

while True:  # Giving while a value means it will cycle until a break is reached

    try:
        number = int(input("Please enter number: "))
        break
    except ValueError:  # Code in except block sends a message related to a specific error
        print("Not a number.")
    except:  # And we can have another block for any other error
        print("Unknown error occurred")
    print("Thank You")

# ---------- File I/O
# Use to store and retreive data from files
# Using 'with' guarantees the file will be closed if the program crashes
# mode w overwrites, mode a appends

#open doesn't open the file, it gives it a handle so that we can read it
with open("myData.txt", mode="w", encoding="utf-8") as my_file:
    # .write can be used to write stuff. Doesn't add a new line.
    my_file.write("Some random text\nMore random text\nMore text")

with open("myData.txt", encoding="utf-8") as my_file:
    print(my_file.read())  # read() gets everyhing at once

print(my_file.closed)  # Returns true if file is closed

# ---------- Classes and Objects
# Classes are blueprints for creating objects


class Square:
    def __init__(self, height="0", width="0"):
        # init sets values for each square
        self.height = height
        self.width = width

    @property  # This is the getter
    def height(self):  # self refers to an object that we don't have a name for
        print("Retreiving the height")
        return self.__height  # __ before private field

    @height.setter  # This is a setter
    def height(self, value):
        if value.isDigit():  # Protects height from receiving a bad value
            self.__height = value
        else:
            print("Please enter a number")

    @property
    def width(self):
        print("Retreiving the width")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isDigit():
            self.__width = value
        else:
            print("Please enter a number")

    def get_area(self):
        return int(self.__width) * int(self.__height)


square = Square() # Create a square object
square.height = "10"
square.width = "10"
print("Area = ", square.get_area())

# ---------- Inheritance and Polymorphism
# With inheritance, a class can inherit all fields and methods of its parent class

class Animal:
    def __init__(self, name="unknown", weight=0):
        self.__name = name
        self.__weight = weight

    @property
    def name(self, name):
        self.__name = name

    def make_noise(self): 
        return "Grrrr"

    def __str__(self): # Used to cast to a string type
        return"{} is a {} and says {}".format(self.__name, type(self).__name__, self.make_noise())

    def __gt__(self, animal2): # Magic method, used for operator overloading
        if self.__weight > animal2.__weight:
            return True
        else:
            return False
# overloading
    # Here I'll define how to evaluate greater
    # than between 2 Animal objects
    # Other Magic Methods
    # __eq__ : Equal
    # __ne__ : Not Equal
    # __lt__ : Less Than
    # __gt__ : Greater Than
    # __le__ : Less Than or Equal
    # __ge__ : Greater Than or Equal
    # __add__ : Addition
    # __sub__ : Subtraction
    # __mul__ : multiplyplication
    # __div__ : Division
    # __mod__ : Modulus

class Dog(Animal): # Dog inherits Animal class
    def __init__(self, name="unknown", owner="unknown", weight=0):
        Animal.__init__(self, name, weight)
        self.__owner = owner

    def __str__(self): # Overriding str function from Animal
        return super().__str__() + " and is owned by " + self.__owner

animal = Animal("Snotty", 100)
print(animal)
dog = Dog("Spot", "John", 150)
print(dog)
print(animal > dog) # Test magic method

# ---------- Threads
# Threads are blocks of code that take turns executing
def execute_thread(i):
# strftime = string formatted time, allows you to define how time is displayed.
    # Print when the thread went to sleep
    print("Thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
   
   # Gen a random sleep time between 1 and 5 sec
    rand_sleep_time = random.randint(1, 5)
    time.sleep(rand_sleep_time) # Pauses code executions for random seconds
    
    # Print info after sleep time
    print("Thread {} stops sleeping at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))

for i in range(10):
    # Every loop a Thread object is created
    # The arguments passed must be a sequence which is why we need comma with 1 arg
    # You pass the Thread object to the function to execute and any args to pass to that method

    thread = threading.Thread(target=execute_thread, args =(i,))
    thread.start()
    # Display active threads
    # The extra 1 is this for loop executing in the main thread
    print("Active Thread: ", threading.activeCount())
    print("Thread Objects: ", threading.enumerate()) # Returns a list of all active thread objects


# ---------- Expressions
# Regular expressions allow you to manipulate strings in powerful ways
# Work almost the same in every programming language

# Used to:
# Search for a specific string in a large amount of data
# Verify string formatting (Email, phone, etc)
# Find and replace strings
# Formatt data into the proper form for exporting

if re.search("ape", "the ape at the apex"):
    print("There is an ape")

allApes = re.findall("ape", "the ape at the apex")
for i in allApes:
    print(i)

the_str = "The ape at the apex"
for i in re.finditer("ape.", the_str):
    loc_tuple = i.span()
    print(loc_tuple)
    print(the_str[loc_tuple[0]:loc_tuple[1]])


# ---------- Networking
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
mysock.connect(('data.pr4e.org', 80)) # make the connection to port 80 on server www.py4e.com
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # GET command according to HTTP protocol
mysock.send(cmd)

while True:
        data = mysock.recv(512) # loop to recceive data in 512 character chunks from sockets
        if (len(data) < 1): # print until there's no more data
            break
        print(data.decode(),end='')
mysock.close()

# urllib library can do the same simple task by treating the website like a file
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())