##########################################
# COMP 354 - Introduction to Engineering
# Project: Learn To Code Like 1,2,3
# Script: STYLE GUIDE
# Author: George Mavroeidis
##########################################

# IMPORTING MODULES

# Wrong:

# Correct:


# WHITE SPACES

my_dict = {
    "brand": "Ford",
    "model": "Mustang",
}

# Correct:
my_dict["brand"]
my_dict[0:1]

# Wrong:
my_dict["brand"]
my_dict[0: 1]

# Correct
x = 1
y = 2
my_big_variable = 3

# Wrong
x = 1
y = 2
my_big_variable = 3

# VARIABLE OPERATIONS

# Correct
x = x + 1
x += 1
y = y*2 + x
z = x*x + y*y
w = (x + y) * (x - y)
w = (x+y) * (x-y)

# Wrong
x = x+1
x += 1
y = y * 2 + x
z = x * x + y * y
w = (x + y) * (x - y)

# FUNCTION ANNOTATIONS

# Correct


def myFunction():
    return 0

# Wrong


def my_function():
    return 0


def MyFunction():
    return 0

# Correct


def myNewFunction(arg1, def_arg=0):
    return arg1 + def_arg

# Wrong


def myNewFunction(arg1, defArg=0):
    return arg1+defArg

# CONDITIONAL STATEMENTS


# Correct
if x == 1:
    x = 0
y = 1
z = x + y

if x == 1 and y == 2:
    x = 0
    y = 1

# Wrong

if x == 1:
    x = 0
y = 1, z = x + y

# NAMING STYLE

# Global Constants (all pascal)
MAX_NUMB = 0

# Local Variables (all lower case)
temp_var = 0

# Class Names


class MyClass:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Class functions
    def myFunction(self):
        return self.num1 + self.num2

# module_name,
# package_name,
# ClassName,
# method_name,
# ExceptionName,
# function_name,
# GLOBAL_CONSTANT_NAME,
# global_var_name,
# instance_var_name,
# function_parameter_name,
# local_var_name

# Exceptions


try:
    print(x)
except NameError:
    print("Something went wrong with a specific exception")
except:
    print("Something went wrong again in other exceptions")
finally:
    print("The 'try except' is finished")

if x < 0:
    raise Exception("Sorry, no numbers below zero")
