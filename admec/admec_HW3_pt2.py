"""
Author: Amanda Manaster
Date: 05/03/2020
Purpose: To get experience using numpy & argparse. Goal of pt 2:
	Have the code save some output to your output directory (admec_output/) as a pickle file, 
	and have it read that file back in. Have the code make the output directory if needed.
"""

#Import necessary libraries
import numpy as np
import pickle
import sys, os

# Part 2: Save some output as a pickle file then read it back in
print('Part 2: Saving pickle files')

# Import my_module
sys.path.append(os.path.abspath('./admec/shared/'))
import my_module as mymod
from importlib import reload
reload(mymod)

# Make sure my output directory exists!
this_dir = os.path.abspath('./admec/').split('/')[-1]
out_dir = './' + this_dir + '_output/'
print('Creating ' + out_dir + ', if needed.')
mymod.make_dir(out_dir)

# Make a new array for funsies
f = np.arange(64).reshape((8,8))

# Save the array as a pickle file
out_fn = out_dir + 'pickle_f.pkl'
pickle.dump(f, open(out_fn, 'wb')) 

# Read the .pkl file back in
g = pickle.load(open(out_fn, 'rb'))

print('\nThe shape of the loaded object is')
print(g.shape)
