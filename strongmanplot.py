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
"""total points graph
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
def total():
  df_total_points=pd.read_csv('input.csv')
  #df_total_points
  plt.bar(x=df_total_points['Heavy wheight Strongman'],
          height=df_total_points['Total points'])
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

    end_time = datetime.datetime.now()    # save the script end time
    print(f'{__file__} took {end_time - start_time} s to complete')
