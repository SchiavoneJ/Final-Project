import datetime  # used for start/end times
import argparse  # This gives better commandline argument functionality
import doctest   # used for testing the code from docstring examples
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('input.csv')
names = df['Heavy wheight Strongman'].values
print(names)