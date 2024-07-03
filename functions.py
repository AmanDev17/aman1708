# definition and syntax of functions
# syntax
# def function name(arguments):

# parameters and arguments
# a)default parameters 
# def grett(name="guest"):
#     print(f"hello",name)

# b)variable length argument- use arqs(*)for variable length arguments #pygame
#                             use kwargs(**)for variable length arguments

# def print_numbers(*args):
#     for number in args:
#        print(number)
# print_numbers(1,2,3,4)

# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")#literals or format

# print_info=(name=("alice"),age=30)

# return values
# it creates a base template of the function 
# jab function ke andar template create karna hota hai toh we use return statements
# it kinda limits the value of variable within the function
# when we compact a setup then it creates cash memory it consists of cash files
# return value tells us that what we have to keep in cash files

def multiply(a,b):
    return a*b
result= multiply(4,5)
print(result)


# without return statement


# scope and lifetime
# global variable it is the default value of variable
# local variable it is used to make customizations
# git github

# anonymous function- changing variable with the same variable for a specific task within the function

# decorators - they are the functions that modify the behaviour of another function (myntra purchase and add to cart)
# syntax
# @function name   static and class method 

# def my_decorator(func):
#     print("something is happening before function")
#     func()
#     print("something is happening after the function")
# return wrapper

# @my_decorator
# def say_hello():
#     print("hello")

# say_hello()


# pipl.org.in(preferred installer program)
# it is a assitant of python
# virtual parameter server====for tom
# modules
# 
# os math re (os is important (operating system))we can update files using os package

# standard library modules
# learn cmd commands for os 

# import os
# print(os.getcwd())   #get the current working directory

# sys module to check the version of System
import sys
print(sys.version)

# dateline module



# http (hyper text transfer protocol )
# communication between client side(browser) and server(host) side is done through http
# it runs query and gives the possible searches present in the


# packages and __init__.py
# init function - passes predefined parameters (predefined labelling)
# syntax
# def__init__(self,var1,var2,var3):


# JSON
import json
data = json.loads('{"name":"alice","age":30}')
print(data['name'])

# random for generating random numbers:
import random
print(random.randint(1,10))

# re for regular expressions
# import re
# pattern=re.compile()



# csv for csv file handling
import csv
with open('data.csv',mode='w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['alice','30'])

