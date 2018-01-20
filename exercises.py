'''

01a Exercises
These exercises should help you get the flavor of how to perform arithmetic and string operations in Python. 
You will also get to play with (pseudo-)random generators and the range operator.
These skills will all be used in assignment 2.

To answer these exercises, open the IDLE program that came with your Python installation. IDLE is a line-by-line Python interpreter.
You can copy lines from this file into IDLE to interpret them and produce a result. Then copy the result back to the following line in this file (after the #).
You will also need to answer several questions to show you understand what is happening. 


'''
# Math in Python is what you would expect. Add comments with the answers the IDLE returns. I'll do the first one for you.
10 + 15 
#25
8 - 1 
#7
10 * 2 
#20
35 / 5
#7

35 / 4
#8.75
35 // 4 
#8
# What is the difference between the / operator and the // operator?
# I was not for sure so I tried to look it up and read that its a difference between floating point division and floor division. I think this means you round down to the nearest whole integer because if you round up it would be more than what is contained by the number. It sort of follows the price is right rules.

2 ** 5 
#32
# What does the ** operator do?
#it is an exponitial command, which is the equivilance to ^ on a calculator. This command is 2 raised to the 5th power.
#
5 % 4
#1
# What does the % operator do?
# according to stackoverflow % in x%m returns a normal remainder modulus, but only if m < x, why is that so? What does % do? How I interpret this is it is sorth of like division without the remainders and rounded down again.

(1 + 3) * 2
#8
# What effect do the parenthesis have on this statement?
#The same rules as basic algebra. If they were not there you would multiply before adding.

# Data in python is of different flavors or "types," each with its own characteristics
type(3)
#<class 'int'>
type(3.0)
#<class 'float'>
type("word")
#<class 'str'>
type(True)
#<class 'bool'>
type(False)
#<class 'bool'>
type(None)
#<class 'NoneType'>
# None is a special object in python. We will talk more about it later


# It is possible to convert from one type to another. 
int(3.0)
#3
float(7)
#7.0
str(55)
#'55'
bool(1)
#True
# How can you tell the difference between these four different types?
#An integer will be a whole number with no decimal, and a float will have decimal numbers. strings will be text, and bool will  be true and falso statements with true returning a 1 and false returning as a 0

# Strings are created with single or double-quotes
"This is a string."
'This is also a string.'

"Hello " + "world!"
# What does the + operator do here?
#'Hello world!' it adds the words together.

"This is a string"[0]
#T
"This is a string"[5]
#i
"This is a string"[8]
#a
# What is happening as you change the number?
#starting with 0 as the T in This, each number represents the next corresponding letter in the string. so "This is a string"[1] would be h and [2] would be i

"This is a string"[-1]
#g
# What happens when you use a negative number?
#it starts in reverse order and reads from end to begining.

"%s can be %s" % ("strings", "interpolated")
# What is happening here? 
#'strings can be interpolated' It puts the statement in the middle of the two words.

# A more robust (and modern) way to put things into strings is using the format method
"{0} can be {1}".format("strings", "formatted")
#'strings can be formatted'

# You can use names instead of numbers to make it easier to keep things straight
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
#'Bob wants to eat lasagna'

# You have already met the print method
print("I'm Python. Nice to meet you!")
# Here is its sibling, the input method
n = input("What is your name? ")
print("Hello, " + n)
#Hello, What is your name?
# What just happened?
# when I copied and pasted it gave me a syntax error but I am pretty sure it is supposed to input What is your name? where n is at.

# For your next assignment, you will need to use random numbers 
# first we need to get a few methods from the library called random
from random import random,randint,shuffle,sample
random()
# Run this line a few times. What is happening here?
# it is randomizing a random decimal or floating number between 0 and 1

randint(1,100)
# How is this different?
#this is a random whole integer between 1 and 100

# The next few use a list of numbers from 0 to 9
items = [0, 1,2,3,4,5,6,7,8,9]
shuffle(items)
print(items)
# What just happened?
# [1, 9, 3, 8, 0, 6, 4, 7, 2, 5] It randomized the order of the set of numbers or items that were listed


print(sample(items, 1))
# What does this do?
# [1] It prints a random item from the sample and prints it out. Mine happened to be 1.

print(sample(items, 5))
# What does the second parameter control?
# [3, 6, 1, 5, 7] This time it printed out 5 random numbers from the items we listed

for i in range(0,5):
	print(i)
# 0
#1
#2
#3
#4
# What is happening here? What happens if you change the two range parameters?
#It vertically listed the range of numbers out instead of horizontally.
