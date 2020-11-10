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

    indx = np.arange(len(subjects))
    score_label = np.arange(0, 10, 1)
    Jordan_means = list(dataset.T['Jordan Koucky'])
    Kealii_means = list(dataset.T['Kealii Kalawao'])
    Andrew_means = list(dataset.T['Andrew Lynch'])
    Gordon_means = list(dataset.T['Gordon Sam'])
    Richard_means = list(dataset.T['Richard Castillo'])
    Zack_means = list(dataset.T['Zack Bunke'])

    bar_width = 0.35
    print(Jordan_means)
    print(Kealii_means)
    print(Andrew_means)
    print(Gordon_means)
    print(Richard_means)
    print(Zack_means)

    fig, ax = plt.subplots()
    barJordan = ax.bar(Jordan_means, bar_width, label='Jordan means')
    barKealii = ax.bar(Kealii_means, bar_width, label='Kealii means')
    barAndrew = ax.bar(Andrew_means, bar_width, label='Andrew means')
    barGordon = ax.bar(Gordon_means, bar_width, label='Gordon means')
    barRichard = ax.bar(Richard_means, bar_width, label='Richard means')
    barZack = ax.bar(Zack_means, bar_width, label='Zack means')

    # inserting x axis label
    ax.set_xticks(indx)
    ax.set_xticklabels(subjects)

    # inserting y axis label
    ax.set_yticks(score_label)
    ax.set_yticklabels(score_label)

    # inserting legend
    ax.legend()

    def insert_data_labels(bars):
        for bar in bars:
            bar_height = bar.get_height()
            ax.annotate('{0:.0f}'.format(bar.get_height()),
                xy=(bar.get_x() + bar.get_width() / 2, bar_height),
                xytext=(0, 3),
                textcoords='offset points',
                ha='center',
                va='bottom'
            )

    insert_data_labels(barJordan)
    insert_data_labels(barKealii)
    insert_data_labels(barAndrew)
    insert_data_labels(barGordon)
    insert_data_labels(barRichard)
    insert_data_labels(barZack)

    plt.show()

    end_time = datetime.datetime.now()    # save the script end time
    print(f'{__file__} took {end_time - start_time} s to complete')
