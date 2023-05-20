from pathlib import Path
import os
import xarray as xr
import pandas as pd

#set where csv will be saved
os.makedirs('/Users/admin/kafka/bdp_assignment/ds', exist_ok=True)

ds = xr.open_dataset('era5_sl_2018_2023.nc')


lat_bnds, lon_bnds = [40, 0], [0,5]
ds = ds.sel(latitude=slice(*lat_bnds), longitude=slice(*lon_bnds))
#view dataset information
print(ds.data_vars)

#add different variables in a datafram (1 col per variable)
df = ds[{'d2m', 't2m', 'istl1', 'istl2', 'istl3', 'istl4', 'msl', 'sst', 'sp', 'tp'}].to_dataframe()

#rename the columns
df = df.rename(columns={'d2m': '2m_dewpoint_temp', 't2m': '2m_temp', 'istl1': 'ice_temp_layer_1', 'istl2': 'ice_temp_layer_2', 'istl3': 'ice_temp_layer_3', 'istl4': 'ice_temp_layer_4', 'msl': 'mean_sea_level', 'sst': 'sea_surface_temp', 'sp': 'surface_pressure', 'tp': 'total_precipitation'})

print(list(df))
print(len(df.index))

df.dropna()

#save dataframe as a .csv file in a given directory
df.to_csv('/Users/admin/kafka/bdp_assignment/ds/era5_sl_2018_2023.csv')
