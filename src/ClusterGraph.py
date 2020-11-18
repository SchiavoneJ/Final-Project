#!/var/env python3
"""! @cluster graph final project
"""
# StrongmanData.py
#
# CPTR 226 
#
# Author: Jared Schiavone
# Date: 2020 November 4
# Version: 1.0
# Course: CPTR 226
# Assignment: cluster grapgh

##
#@mainpage cluster graph stats of strongmen 


# Includes
import datetime  # used for start/end times
import argparse  # This gives better commandline argument functionality
import doctest   # used for testing the code from docstring examples
import matplotlib.pyplot as plt #used to graph data
import pandas as pd #used to graph data
import numpy as np #used to graph data
import pdb #used to graph data

# Global Variables


# Functions
"""reading the csv pulling out the groups
"""
def graph():
    """! this functions takes inputs and creates a sentence

    @param subject        takes all titles in csv
    @param groupby        takeing only the names and grouping them

    @return dataset

    """
    df = pd.read_csv('input.csv')
    subjects_all = list(df)
    subjects = subjects_all[1:-1]
    col_all = list(df)
    col = col_all[2:-1]
    dataset = df.groupby('Heavy wheight Strongman')[subjects].mean()
    names = df['Heavy wheight Strongman']
    print(names)
    # set width of bar
    barWidth = 0.1

    # set height of bar
    heights = []
    for name in names:
        heights.append(list(dataset.T[name]))
    print(heights)

    # Set position of bar on X axis
    bar_x = [np.arange(len(heights[0]))]
    for bar in np.arange(1,len(names)):
        bar_x.append([x + barWidth for x in bar_x[bar -1]])

    # Make the plot
    for idx in np.arange(len(names)):
        plt.bar(bar_x[idx], heights[idx], width=barWidth, edgecolor='white', label=names[idx])

    # Add xticks on the middle of the group bars
    plt.xlabel('GROUPS', fontweight='bold', fontsize='13')
    plt.xticks([r + barWidth*2.5 for r in range(len(col))], col, fontsize='13')
    plt.ylabel('POINTS', fontweight='bold', fontsize='13')

    # Create legend & Show graphic
    plt.legend()
    plt.show()

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
    #this tells it to graph
    graph()
    
    end_time = datetime.datetime.now()    # save the script end time
    print(f'{__file__} took {end_time - start_time} s to complete')
