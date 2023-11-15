# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:07:28 2023

@author: erlde
"""

import csv

champs = {'2020': {'Warriors', 'Suns', 'Nuggets', 'Lakers'},
          '2010': {'Warriors', 'Spurs', 'Thunder', 'Mavericks', 'Lakers'},
          '2000': {'Lakers', 'Spurs', 'Mavericks'},
          '1990': {'Trail Blazers', 'Lakers', 'Suns', 'Rockets', 'SuperSonics', 'Jazz', 'Spurs'},
          '1980': {'Lakers', 'Rockets'},
          '1970': {'Lakers', 'Bucks', 'Warriors', 'Suns', 'Trail Blazers', 'SuperSonics'},
          '1960': {'Hawks', 'Lakers', 'Warriors'}}

# Create a CSV file and write the header
with open('champs1.csv', 'w', newline='') as csvfile:
    fieldnames = ['Year', 'Champions']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()

    # Write data to CSV file
    for year, teams in champs.items():
        writer.writerow({'Year': year, 'Champions': ', '.join(teams)})