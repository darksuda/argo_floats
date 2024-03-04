import netCDF4 as cdf 
import numpy as np
import matplotlib.pyplot as plt

file = 'assets\COPERNICUS_DWNLDS\oxy.nc'
data = cdf.Dataset(file)

print(data)

fig, ax = plt.subplots()

ax.contourf