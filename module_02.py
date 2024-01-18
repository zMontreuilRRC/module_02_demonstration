"""
Description: Module 02 Demonstration
Author: Zacharie Montreuil
Date: 16 January 2024
Usage: Demonstrate content from Module 02
"""

# Constants
PI = 3.14159
DAYS_IN_YEAR = 365
# Purely convention; these can be changed 

# Function
# A unit of code that can be re-used repeatedly

# () parentheses contain "arguments"
# the function runs using the arguments that have been provided
print("test value")

print(5)

# order of operations
# evaluates (finds the outcome) of the operation before using it as an argument
print(3 + 3)

# abs function: "Absolute value" of number argument
# argument: -50
# "invocation" : when a function is "called" or "used"
# "return value": the value that the function invocation is evaluated 
# to/replaced by
print( 
    abs(-50) #output 50
)
"""
print(50)
"""

print("I am", 25, "years old")

"""
DATA TYPES
"""

# variables
# something used for storing a value

# DECLARE variable "number_a" and ASSIGN value of 12
number_a = 12

# RE-ASSIGN number_a with value 13
number_a = 13
number_b = 25

# Declare number_sum and assign it the evaluation of number_a + number_b values
number_sum = number_a + number_b
print(number_sum)

# Variable Type
# Numeric types
# integer
new_int = 32

# floating points
new_float = 32.7

# Text Types
# strings --collections of characters 
new_str = "This is a string"

# Boolean types
new_bool = False
print(type(new_bool))

# Programming Languages are typically either DYNAMICALLY or STRICTLY typed

age = 25
current_salary = 67293.21

# "implicitly" convert age to a float for this operation
age_and_salary = age + current_salary
print(age_and_salary)

months = "October"
years = "Twenty-twenty-four"
era = "Twenty-fungalore"

print(months + years)

# String methods
original_string = "hello world"

original_string = original_string.capitalize() # assign original_string variable to the return value of original_string.capitalize
print(original_string)

"""
Find the arguments that must be passed and return values of these string methods
center()
startswith()
endswith()
upper(), lower()
len()
"""
firstoperand = 12
secondoperand = 30

importantpower = firstoperand ** secondoperand

"""
Collections
"""

#list: ordered, mutable, index-referenced collection
new_list = ["test", 3, True, 5 , 3]
second_value = new_list[1]
new_list.append("new element")
new_list[2] = "reassigned value"
print(new_list)

#tuples: like lists but immutable
new_tuple = ("first", "second", True)

#dictionary: unordered, mutable, key-value pairs
new_dictionary = {
    "first_key": 5, 
    12: "twelve"
}

new_dictionary[12] = "thirteen"

# set: non-repeating values
new_set = {4, 5, 6, 7, 7, 8}
two_set = {5,5,8}
# how do I get all of the common values between these two sets?
"""

Use Python's set intersection:

>>> list1 = [1,2,3,4,5,6]
>>> list2 = [3, 5, 7, 9]
>>> list(set(list1).intersection(list2))
[3, 5]
"""
# https://stackoverflow.com/a/2864863

intersection = new_set.intersection(two_set)
print(intersection)