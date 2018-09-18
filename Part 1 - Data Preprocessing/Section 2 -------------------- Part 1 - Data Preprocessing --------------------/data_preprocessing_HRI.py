# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 12:17:03 2018

@author: HRI
"""

# Importing the libraries

import numpy as np

import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values

y = dataset.iloc[:, 3].values



