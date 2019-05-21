# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:40:18 2019

@author: Matthew Wolf
"""

def support(sector, projects):
    """========================================================================
    Returns support of sector from list of sector-tagged projects.
    
    INPUT:   sector   - Tuple, ('sector-vocabulary-code','sector-code')
             projects - list of tuples, representing sectors tagged to project
    OUTPUT:  float
    ========================================================================"""
    # count of occurences of sector
    occurences = 0
    # for each project
    for project in projects:
        # check if it is tagged with the sector of interest
        if sector in project:
            # if so up the count
            occurences += 1
    # return the proportion of occurences (the support)
    return occurences / len(projects)

def confidence(sectorA, sectorB, projects):
    """========================================================================
    Returns confidence of sectorA in projects containing sectorB from list of 
    sector-tagged projects.
    
    INPUT:   sectorA   - Tuple, ('sector-vocabulary-code','sector-code')
             sectorB   - Tuple, ('sector-vocabulary-code','sector-code')
             projects  - list of tuples, representing sectors tagged to project
    OUTPUT:  float
    ========================================================================"""
    # count of occurences of sectorB
    occurencesB = 0
    # for each project
    for project in projects:
        # check if it is tagged with the sector of interest
        if sectorB in project:
            # if so up the count
            occurencesB += 1
    # count the co-occurences of sectorA and sectorB
    occurencesAB = 0
    # for each project 
    for project in projects:
        # check if sectorA and sectorB co-occur
        if sectorA in project and sectorB in project:
            # if so up the count
            occurencesAB += 1
    # return the confidence of A over B
    return occurencesAB / occurencesB

def lift(sectorA, sectorB, projects):
    """========================================================================
    Returns lift of sectorA over sectorB in projects from list of 
    sector-tagged projects.
    
    INPUT:   sectorA   - Tuple, ('sector-vocabulary-code','sector-code')
             sectorB   - Tuple, ('sector-vocabulary-code','sector-code')
             projects  - list of tuples, representing sectors tagged to project
    OUTPUT:  float
    ========================================================================"""
    # lift if confidence over support
    return confidence(sectorA, sectorB, projects) / support(sectorB, projects)

def create_sector_list(data):
    """========================================================================
    Returns lift of sectorA over sectorB in projects from list of 
    sector-tagged projects.
    
    INPUT:   sectorA   - Tuple, ('sector-vocabulary-code','sector-code')
             sectorB   - Tuple, ('sector-vocabulary-code','sector-code')
             projects  - list of tuples, representing sectors tagged to project
    OUTPUT:  float
    ========================================================================"""
    sector_list = []
    for project in data:
        for sector_tuple in project:
            if sector_tuple not in sector_list:
                sector_list.append(sector_tuple)
    return sector_list


