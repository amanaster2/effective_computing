"""
Author: Amanda Manaster
Date: 05/03/2020
Purpose: To get experience using numpy & argparse. Goal of pt 3:
	Use argparse to add command-line arguments to your code, allowing the user to make 
	some choice about what happens.
"""
# Import necessary libraries
import argparse

# Function to more easily accept Boolean input
def boolean_string(s):
    if s not in ['False', 'True']:
        raise ValueError('Not a valid boolean string')
    return s == 'True'

# Part 3: Use argparse to add command-line arguments to code
print('Part 3: Using argparse')

# Create parser object
parser = argparse.ArgumentParser()

# Define some arguments that can be passed to this script
parser.add_argument('-n', '--name_string', default='Anonymous', type=str)
parser.add_argument('-a', '--age_integer', default=21, type=int)
parser.add_argument('-g', '--gpa_float', default=4.0, type=float)
parser.add_argument('-s', '--student_verbose', default=True, type=boolean_string)

# Get the arguments from the command line
args = parser.parse_args()

# Print some output
print('\nYour name is ' + args.name_string.capitalize() + '.')
print('\nYou are', args.age_integer, 'years old.' )

if args.student_verbose:
    print('\nYour GPA is ' + str(args.gpa_float) + '.')
else:
	raise Exception('You are not a student. You do not have a GPA.')