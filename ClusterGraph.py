#!/var/env python3
#
# StrongmanData.py
#
# CPTR 226 
#
# Author: Jared Schiavone
# Date: 2020 November 4
# Version: 1.0
# Course: CPTR 226
# Assignment: 
"""cluster graph
"""

# Includes
import datetime  # used for start/end times
import argparse  # This gives better commandline argument functionality
import doctest   # used for testing the code from docstring examples
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Global Variables


# Functions

# This runs if the file is run as a script vs included as a module
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--doctest', action='store_true',
                        help='Pass this flag to run doctest on the script')
    start_time = datetime.datetime.now()  # save the script start time
    args = parser.parse_args()  # parse the arguments from the commandline

    if(args.doctest):
        doctest.testmod(verbose=True)  # run the tests in verbose mode

    print("-------------------")
    df = pd.read_csv('input.csv')
    subjects = ['Heavy wheight Strongman', 'Log Clean and Press',
                'Farmers Carry w/ Keg Carry', 'Deadlift', 'Yolk & Tire Flip',
                'Stones of Steel over a Bar']

    dataset = df.groupby('Heavy wheight Strongman')[subjects].mean()

    # set width of bar
barWidth = 0.1
 
# set height of bar
Jordan_means = list(dataset.T['Jordan Koucky'])
Kealii_means = list(dataset.T['Kealii Kalawao'])
Andrew_means = list(dataset.T['Andrew Lynch'])
Gordon_means = list(dataset.T['Gordon Sam'])
Richard_means = list(dataset.T['Richard Castillo'])
Zack_means = list(dataset.T['Zack Bunke'])

# Set position of bar on X axis
r1 = np.arange(len(Jordan_means))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
 
# Make the plot
plt.bar(r1, Jordan_means, color='#ff0000', width=barWidth, edgecolor='white', label='Jordan Koucky')
plt.bar(r2, Kealii_means, color='#0000ff', width=barWidth, edgecolor='white', label='Kealii Kalawao')
plt.bar(r3, Andrew_means, color='#008000', width=barWidth, edgecolor='white', label='Andrew Lynch')
plt.bar(r4, Andrew_means, color='#800080', width=barWidth, edgecolor='white', label='Gordon Sam')
plt.bar(r5, Andrew_means, color='#ffa500', width=barWidth, edgecolor='white', label='Richard Castillo')
plt.bar(r6, Andrew_means, color='#00fff9', width=barWidth, edgecolor='white', label='Zack Bunke')

# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold', Fontsize='13')
plt.xticks([r + barWidth*2.5 for r in range(len(Jordan_means))], ['Log Clean and Press', 'Farmers Carry w/ Keg Carry', 'Deadlift',
                                                                  'Yolk & Tire Flip', 'Stones of Steel over a Bar'], Fontsize='13')
 
# Create legend & Show graphic
plt.legend()
plt.show()


end_time = datetime.datetime.now()    # save the script end time
print(f'{__file__} took {end_time - start_time} s to complete')
