import netCDF4 as cdf
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap 
from numpy import meshgrid
import pandas as pd
import json
import numpy as np


datadf = cdf.Dataset('assets\COPERNICUS_DWNLDS\TSM_COP_13_SEP_PERU.nc')

lat = np.array(datadf['latitude'])
lon = np.array(datadf['longitude'])
time = np.array(datadf['time'])



tempdf = pd.DataFrame()

sst = np.array(datadf['thetao'])
sst[ sst==9.96921e+36] = np.NaN
sst_m = np.mean( np.array([ sst[0][0]]), axis=0 )


xx, yy = meshgrid(lon, lat)

floatsdf = json.load(open('assets\ARGOS_DWNLDS\data_SEP_2023.json'))

lats = []
lons = []
dates = []

for i in floatsdf:
        lons.append(i['geolocation']['coordinates'][0])
        lats.append(i['geolocation']['coordinates'][1])
        dates.append(i['timestamp'][0:10])


fig = plt.figure(figsize = (16,9))

m = Basemap(projection='merc',
        llcrnrlat = -22, #Lower Left Corner Latitud   SOUTH
        urcrnrlat = 0,  #Upper Right Corner Latitud   NORTH
        llcrnrlon = -86, #Lower Left Corner Longitud   WEAST
        urcrnrlon = -68,  #Upper Right Corner Longitud  EAST
        resolution='h'
        )

m.drawcoastlines()
m.drawcountries()

m.drawparallels(np.linspace(0,-22, 12), labels=[True, False, False, False])
m.drawmeridians(np.linspace(-86,-68,10), labels=[False, False, False, True])

plot1 = m.contourf(xx, yy, sst_m, cmap= 'rainbow', levels = np.linspace(13,31, 19), latlon=True)
plot2 = m.contour(xx, yy, sst_m, levels = np.arange(15, 31, 1), colors= 'black', linewidths= 0.2, latlon=True)
plt.clabel(plot2, inline=True, fontsize=7.5, colors = 'black')
m.fillcontinents('white')

a_floats = m.scatter(lons, lats, latlon = True, s=80, color='#ffff00', edgecolors="#000a2e", label='Argo floats')

cbar = plt.colorbar(plot1, ticks = np.linspace(13,31, 19), label = 'Temperature (°C)')
plt.title('Argo Floats en la costa peruana\nSEPTIEMBRE 2023')
plt.xlabel('Longitud', labelpad=25)
plt.ylabel('Latitud', labelpad=35)

plt.legend(loc='center left', bbox_to_anchor=(0.8, -0.10))


plt.figtext(0.4, 0.02, "Fuente:\n - Argo (https://argo.ucsd.edu)\n - Copernicus Marine Service (https://marine.copernicus.eu)", fontsize=6.5)
#plt.savefig('assets\BE\PLOTS/Map_argo_16_18_mar')
plt.show()

"""
"""