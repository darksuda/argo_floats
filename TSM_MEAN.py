import netCDF4 as cdf
import numpy as np
import pandas as pd


data = 'assets\COPERNICUS_DWNLDS\TSM AREAS\TSM ILO 1998.nc'

print(cdf.Dataset(data)['thetao'])
tsm = np.array(cdf.Dataset(data)['thetao'])

tsm[tsm == -32767] = np.NaN
tsm[tsm == 9.96921e+36] = np.NaN


tsm_daily_mean = []

for i in tsm:
    tsm_daily_mean.append(np.nanmean(i[0]))

datadf = pd.DataFrame(tsm_daily_mean)
datadf.columns = ['Ilo']

print(datadf)
datadf.to_csv('assets/CSVs/tsm_ilo_1998.csv', index=False)


print(np.array(cdf.Dataset(data)['longitude']))
print(np.array(cdf.Dataset(data)['latitude']))




