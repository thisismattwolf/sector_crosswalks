# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:23:16 2019

@author: Matthew Wolf
"""

import pandas as pd
from data_prep import data_prepare

# get the World Bank sector and sector codes data
data = data_prepare()

from functions import support, confidence, lift, create_sector_list

sector_list = create_sector_list(data)

lifts = [[sector[0],sector[1],support(sector, data)] for sector in sector_list]

#TO-DO 1. Need to calculate frequency of individual sector codes

frequencies = {}

for row in data:
    for sector in row:
        if sector[1] not in frequencies.keys():
            frequencies[sector[1]] = 1
        else:
            frequencies[sector[1]] += 1

        

#TO-DO 2. Then calculate lift of  