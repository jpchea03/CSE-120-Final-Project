# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:28:08 2023

@author: erlde
"""

import pandas as pd

champs = {'2020': {'Warriors', 'Suns', 'Nuggets', 'Lakers'},
          '2010': {'Warriors', 'Spurs', 'Thunder', 'Mavericks', 'Lakers'},
          '2000': {'Lakers', 'Spurs', 'Mavericks'},
          '1990': {'Trail Blazers', 'Lakers', 'Suns', 'Rockets', 'SuperSonics', 'Jazz', 'Spurs'},
          '1980': {'Lakers', 'Rockets'},
          '1970': {'Lakers', 'Bucks', 'Warriors', 'Suns', 'Trail Blazers', 'SuperSonics'},
          '1960': {'Hawks', 'Lakers', 'Warriors'}}

# Create a DataFrame from the dictionary
df = pd.DataFrame(list(champs.items()), columns=['Year', 'Champions'])

# Convert the set of champions to a comma-separated string
df['Champions'] = df['Champions'].apply(lambda x: ', '.join(x))

# Save the DataFrame to a CSV file
df.to_csv('champs.csv', index=False)
