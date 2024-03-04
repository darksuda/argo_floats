import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from cartopy import crs as ccrs, feature as cfeature
import netCDF4 as cdf
import json
from datetime import datetime, timedelta

file = 'assets\COPERNICUS_DWNLDS\global-analysis-forecast-bio-001-028-daily_1697726842431.nc'
data = cdf.Dataset(file)

si = np.array(data['si'])[0][0]
si[si == 9.96921e+36] = np.nan
lat = np.array(data['latitude'])
lon = np.array(data['longitude'])
print(si.shape)



projPC = ccrs.PlateCarree()
lonW = -86 
lonE = -68
latS = -22
latN = 0
res = '10m'

fig = plt.figure(figsize=(8, 8.5))
ax = plt.subplot(1, 1, 1, projection=projPC)


ax.set_extent([lonW, lonE, latS, latN], crs=projPC)
ax.coastlines(resolution=res, color='black')
ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='black', linestyle='--')
ax.set_xticks(np.arange(-86, -67.9, 2))
ax.set_xticklabels(['86°W', '84°W', '82°W', '80°W', '78°W', '76°W', '74°W', '72°W', '70°W', '68°W'])
ax.set_yticks(np.arange(-22, 0.1 , 2))
ax.set_yticklabels(['22°S', '20°S', '18°S', '16°S', '14°S', '12°S', '10°S', '8°S', '6°S', '4°S', '2°S', '0°N'])


ax.set_title('Oxigeno disuelto a 20m de profundidad\n19 de octubre del 2023', fontsize= 15)
plot = ax.contourf(lon, lat, si, levels = np.arange(0, 37, 2))
plot2 = ax.contour(plot, levels = [10, 20, 25, 30], colors = 'white', linewidths = 0.8)
ax.clabel(plot2)

plt.colorbar(plot, label = 'Concentración de silicatos (mmol/m3)')

plt.grid()
plt.show()