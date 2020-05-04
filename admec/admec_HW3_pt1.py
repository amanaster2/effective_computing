""" 
Author: Amanda Manaster
Date: 05/03/2020
Purpose: To get experience using numpy & argparse. Goal of pt 1:
	Make some arrays in numpy and try 5 methods of your choice on them.
"""

#Import necessary libraries
import numpy as np
import pickle
import sys, os

# Part 1: Make some arrays in numpy & try 5 methods.
print('Part 1: Using numpy methods')
# Initialize arrays
a = np.linspace(0,1,5)
b = np.zeros((4,2))
c = np.array([[3, 6, 9, 12, 15], 
			  [18, 21, 24, 27, 30]])
d = np.arange(13)
e = np.full((6,6), 13)

# Print out information about the arrays and the arrays themselves
print("Array a is", a.size, "elements long with shape",
 	   a.shape,"and was created using np.linspace().")
print(a)
print("\nArray b is", b.size, "elements long with shape",
	   b.shape,"and was created using np.zeros().")
print(b)
print("\nArray c is", c.size, "elements long with shape",
 	   c.shape, "and was created using np.array().")
print(c)
print("\nArray d is", d.size, "elements long with shape",
  	   d.shape, "and was created using np.arange().")
print(d)
print("\nArray e is", e.size, "elements long with shape",
	  e.shape, "and was created using np.full().")
print(e)

# Method 1
print("\nWe can cube array a:")
print(a**3)
# Method 2
print("\nWe can change one of the elements of array b:")
b[2, 1]=32
print(b)
# Method 3
print("\nWe can take the square root of array c:")
print(np.sqrt(c))
# Method 4
print("\nWe can make a boolean mask for array d. \n"
	  "Suppose we want to know what elements are >= 7. \n"
	  "We first make the mask array:")
mask = d >= 7
print(mask)
print("Then we apply the mask to array d:")
dd = d[mask]
print(dd)
# Method 5
print("\nWe can flatten array e:")
print(e.flatten())