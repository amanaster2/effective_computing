# import modules
import sys, os
sys.path.append(os.path.abspath('shared'))
import my_module

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Specify input directory
in_dir = '../admec_input/'

# Create output directory/make sure output directory exists
out_dir = '../admec_output/'
my_module.make_dir(out_dir)

# Specify input file
in_fn = in_dir + '2017-01-0118.ctd'

# Name output files
out_fn_1 = out_dir + 'out_test_1.png'
out_fn_2 = out_dir + 'out_test_2.png'

# Method 1: use open() and for loop
with open(in_fn, 'r', errors='ignore') as f:
    get_data = False
    depth = []
    temp = []

    for line in f:
        if ('END OF HEADER' in line) and (get_data==False):
            get_data = True
        elif get_data == True:
            LS = line.split() # split items on line into strings
            depth.append(-float(LS[1]))
            temp.append(float(LS[2]))
f.close()

# Plot the data
plt.close('all')
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(temp, depth, 'ob')
ax.grid(True)
ax.set_xlabel('Temperature [deg C]')
ax.set_ylabel('Z [m]')
ax.set_title(in_fn + ': from scratch')
plt.show()
plt.savefig(out_fn_1)

# Method 2: use pandas.read_csv()
# Read in data
df = pd.read_csv(in_fn, skiprows=571, header=None, delim_whitespace=True)
df['Z [m]'] = -df[1] # add Z column

# Plot the data
fig1, ax1 = plt.subplots(figsize=(8,8))
df.plot(x=2, y='Z [m]', style='og', legend=False, grid=True,
    title=in_fn +': using Pandas', ax=ax1)
ax1.set_xlabel('Temperature [deg C]')
ax1.set_ylabel('Z [m]')
plt.show()
plt.savefig(out_fn_2)