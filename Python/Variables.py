# Variable is a box containing something
# can contain letters, underscores, numbers
# no starting with number
# No special characters
# No length specified for name of variable
# String, characters, float, integer
# No difference between single/double quotes 
# Printing will bring all things to console
# print()- some action is performed
a = 5
b = 10
my_variable = 56
any_variable_name = 100

string_variable = "hello"
single_quotes = 'strings can have single quotes'

print(string_variable)
print(my_variable)

# print is a method with one parameter—what we want to print

### FUNCTION section
# Indentation is necessary
# 'def' keyword
# Parameters of function

# Function 1

def my_print_method(my_parameter):                      # function's definition
    print(my_parameter)

my_print_method(string_variable)                        # calling of function


# Function 2

def my_multiplication_method(number_one, number_two):
    return number_one * number_two                      # returning a value

result = my_multiplication_method(a, b)
print(result)

print(my_multiplication_method(56, 75))

my_print_method(my_multiplication_method('b', 5))  # What would this do?`

''' function within function '''

''' pass means do nothing '''