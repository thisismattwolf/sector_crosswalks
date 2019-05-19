# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:08:57 2019

@author: Matthew Wolf
"""

import pandas as pd

#==================================
#1. FILTER FOR THE DATA WE NEED
# We want two columns - the sector codes and the sector vocabulary codes.
# We only want rows with valid values for both of these.
#==================================

# Import only the sectors columns from the WBG data
data = pd.read_csv('WBG_IATI_Activities_20190315.csv', usecols=['reporting-org',\
                                                             'sector-code', \
                                                             'sector-vocabulary-code'])

# The data contains 30 rows of incomplete data with the reporting-org
# "World Bank Group" instead of "World Bank"
data.drop(data[data['reporting-org'] == 'World Bank Group'].index, inplace=True)

# reset the index
data = data.reset_index()

# delete the resulting 'index' column which has the old index names
del data['index']

# delete the reporting-org column - we don't need it anymore
del data['reporting-org']

#==================================
#2. PREPARE THE DATA
# We want two columns - the sector codes and the sector vocabulary codes.
# We only want rows with valid values for both of these.
#==================================
# sector-code and sector-vocabulary-code contain strings that are really ;-delimited
# lists of sector codes and sector vocab codes.
# Convert these to lists.
for i in data.index:
    #print('Line: ' + str(i))
    data.at[i, 'sector-code'] = data.at[i, 'sector-code'].split(';')
    data.at[i, 'sector-vocabulary-code'] = data.at[i, 'sector-vocabulary-code'].split(';')
    #result = list(zip(data.at[i,'sector-vocabulary-code'], data.at[i, 'sector-code']))
    #print(list(result))
    #data.at[i, 'sectors-zipped'] = [x[0] + '-' + x[1] for x in result]
#TODO - this line is intended to create a new column that concatenates the 
#sector code and sector vocab code in the loop. Not working - fix later
    #data.at[i, 'zipped'] = [x + '-' + y for x,y in zip(data.at[i, 'sector-code'],data.at[i, 'sector-vocabulary-code'])]











