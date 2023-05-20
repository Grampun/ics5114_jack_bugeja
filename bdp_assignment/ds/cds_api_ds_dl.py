#!/usr/local/lib/ python3.10
import cdsapi

# c = cdsapi.Client()

# c.retrieve(
#     'reanalysis-era5-single-levels',
#     {
#         'product_type': 'ensemble_mean',
#         'variable': [
#             '2m_dewpoint_temperature', '2m_temperature', 'ice_temperature_layer_1',
#             'ice_temperature_layer_2', 'ice_temperature_layer_3', 'ice_temperature_layer_4',
#             'mean_sea_level_pressure', 'sea_surface_temperature', 'surface_pressure',
#             'total_precipitation',
#         ],
#         'year': [
#               #'2006', '2007', '2008',
#               #'2009', '2010', '2011',
#             #'2012', '2013', '2014',
#             #'2015', '2016', '2017',
#             '2018', '2019', '2020',
#             '2021', '2022', '2023',
#         ],
#         'month': [
#             '01', '02', '03',
#             '04', '05', '06',
#             '07', '08', '09',
#             '10', '11', '12',
#         ],
#         'day': [
#             '02', '04', '06',
#             '08', '10', '12',
#             '14', '16', '18',
#             '20', '22', '24',
#             '26', '28', '30',
#         ],
#         'time': [
#             '00:00', '03:00', '06:00',
#             '09:00', '12:00', '15:00',
#             '18:00', '21:00',
#         ],
#         'area': [
#             51, 0, 0,
#             10,
#         ],
#         'format': 'netcdf',
#     },
#     'era5_sl_2018_2023.nc')

c = cdsapi.Client()

c.retrieve(
    'satellite-sea-level-mediterranean',
    {
        'variable': 'all',
        'format': 'zip',
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'year': [
            '2012', '2013', '2014',
            '2015', '2016', '2017',
            '2018', '2019', '2020',
        ],
        'day': [
            '02', '04', '06',
            '08', '10', '12',
            '14', '16', '18',
            '20', '22', '24',
            '26', '28', '30',
        ],
    },
    'sea_level_daily_2012_2020.zip')
