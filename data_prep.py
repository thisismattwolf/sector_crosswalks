# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:08:57 2019

@author: Matthew Wolf
"""

def data_prepare():

    import pandas as pd
    
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
    
    #list to hold the results
    result = []
    
    # iterate through the rows. for each row...
    for i in data.index:
        
        # ... split the sector codes, which are delimited with ';'
        data.at[i, 'sector-code'] = data.at[i, 'sector-code'].split(';')
        
        # ... split the sector vocab codes, also delimited with ';'
        data.at[i, 'sector-vocabulary-code'] = data.at[i, 'sector-vocabulary-code'].split(';')
        
        # ... and zip the two split lists together and convert to a list of tuples
        # append this list of tuples to the results list of lists
        result.append(list(zip(data.at[i,'sector-vocabulary-code'], data.at[i, 'sector-code'])))
    
    # return the list of lists of tuples. Each list of tuples is a project,
    # each tuple a tagged sector code and its sector vocab code
    return result









