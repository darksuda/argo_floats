import netCDF4 as cdf
import numpy  as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from numpy import meshgrid


datadf = cdf.Dataset('assets\BE\sst_an.nc')

lat = np.array(datadf['lat'])
lon = np.array(datadf['lon'])
time = np.array(datadf['time'])
analysed_sst = np.array(datadf['sst_anomaly'])[0]
analysed_sst[analysed_sst == -32768] = np.NaN


xx, yy = meshgrid(lon, lat)

fig = plt.figure(figsize = (16,9))
print(analysed_sst)
m = Basemap(projection='merc',
        llcrnrlat = -22, #Lower Left Corner Latitud   SOUTH
        urcrnrlat = 0,  #Upper Right Corner Latitud   NORTH
        llcrnrlon = -86, #Lower Left Corner Longitud   WEAST
        urcrnrlon = -68,  #Upper Right Corner Longitud  EAST
        resolution='h'
        )

m.drawcoastlines()
m.drawcountries()

m.drawparallels([-18,-10,-3,0], labels=[True, False, False, False])
m.drawmeridians(np.arange(-85,-68,2), labels=[False, False, False, True])

plot1 = m.contourf(xx, yy, analysed_sst, cmap= 'RdYlBu_r', levels = np.linspace(-7,7,11), latlon=True)
plot2 = m.contour(xx, yy, analysed_sst, levels = np.linspace(-7,7,11), colors= 'black', linewidths= 0.5, latlon=True)
plt.clabel(plot2, inline=True, fontsize=10, colors = 'black')
m.fillcontinents('white')

cbar = plt.colorbar(plot1, ticks = np.linspace(-7,7,11))
plt.show()
"""
"""