# Yiannis Charalambous - 2021

# To run this python file. cd to this folder in cmd.
# Then run the command python3 name_of_file.py

# Each python command is ran line by line from top to bottom.
# Comments won't be interpreted as commands. You can create a
# comment using #, anything on that line towards the right is
# a comment.
apples = 3

# You have assigned the number 3 to a variable...

# Let's do some maths to our apples variable.
apples = apples + 1
apples = apples * 2 
apples = apples / 2
apples = apples - 2

# This is a variable storing a string, string is a collection
# of characters, so text basically.

message = "Hello world"

print(message)

print("You have " + str(apples) + " apples.")

# The line above prints one string, that one string is combined from
# multiple strings. When the + operator is used between strings, it
# creates a bigger string.

# The str(apples) is a function call to convert apples into a string.
# Since apples was not created as a string initially, it was created
# as a number.

# Functions are re-usable pieces of code, you can supply parameters
# that affect the way they work. Functions can also return variables.

# Let's create a function that adds two numbers and returns the result.
# This is a pretty redundant function but it's for learning :)

def add_number(first_number, second_number):
	# Stuff that is indented belongs to our function.
	result = first_number + second_number
	
	# The line below will tell the function to stop
	# executing and return to the line that called it,
	# it will also return that number stored in the
	# variable result as a return value.
	return result

# We can call our function now from any place after we have declared it,
# this is because the python interpreter reads line by line, so it won't
# know about add_number before it discovers it.
final_number = add_number(1, 2)

print(str(final_number))

final_number = add_number(apples, 1)

print(str(final_number))

# Challenge: Figure out why this returns 4
final_number = add_number(-1, 5)

print(final_number)
