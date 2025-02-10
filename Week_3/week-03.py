# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aSeOQI7X3K0lZABM8FRtuoR6D9stL8UP
"""

#%%% imports
import numpy as np
import pandas as pd
import cProfile

from google.colab import drive
drive.mount('/content/drive')

# %% read in the data
df = pd.read_excel("/content/clinics.xls") # Use pd.read_excel instead of pd.read_xls
print(df.head())

#%% define the distance computation function
# Define a basic Haversine distance formula
def haversine(lat1, lon1, lat2, lon2):
    MILES = 3959
    lat1, lon1, lat2, lon2 = map(np.deg2rad, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    total_miles = MILES * c
    return total_miles

#%% define a function to compute distance, using a for loop
# Define a function to manually loop over all rows and return a series of distances
def haversine_looping(df):
    distance_list = []
    for i in range(0, len(df)):
        d = haversine(40.671, -73.985, df.iloc[i]['locLat'], df.iloc[i]['locLong'])
        distance_list.append(d)
    return distance_list
cProfile.run("df['distance'] = haversine_looping(df)")

#%% Vectorized Haversine computation using iterrows with dynamic column names
def haversine_iterrows(df):
    haversine_series = []

    # Identify the correct column names dynamically
    latitude_col = next((col for col in df.columns if col.lower() in ['latitude', 'loclat']), 'latitude')
    longitude_col = next((col for col in df.columns if col.lower() in ['longitude', 'loclong']), 'longitude')

    for _, row in df.iterrows():
        haversine_series.append(haversine(40.671, -73.985, row[latitude_col], row[longitude_col]))

    return haversine_series

# Run profiling on the function
cProfile.run("df['distance'] = haversine_iterrows(df)")

# Commented out IPython magic to ensure Python compatibility.
# #%%% Optimize further
# 
# # Timing apply on the Haversine function
# %%timeit
# # Use the correct column names 'locLat' and 'locLong' instead of 'latitude' and 'longitude'
# df['distance'] = df.apply(lambda row: haversine(40.671, -73.985, row['locLat'], row['locLong']), axis=1)
# 
# 
#

# Commented out IPython magic to ensure Python compatibility.
# #%lprun -f haversine df.apply(lambda row: haversine(40.671, -73.985, row['locLat'], row['locLong']), axis=1)
# #%%
# %%timeit
# # Vectorized implementation of Haversine applied on Pandas series
# df['distance'] = haversine(40.671, -73.985, df['locLat'], df['locLong'])
#

#%%
cProfile.run("df['distance'] = haversine(40.671, -73.985, df['locLat'], df['locLong'])")

# Commented out IPython magic to ensure Python compatibility.
# #%%
# %%timeit
# # Vectorized implementation of Haversine applied on NumPy arrays
# df['distance'] = haversine(40.671, -73.985, df['locLat'].values, df['locLong'].values)

#%%
cProfile.run("df['distance'] = haversine(40.671, -73.985, df['locLat'].values, df['locLong'].values)")