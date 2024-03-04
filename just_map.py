import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from cartopy import crs as ccrs, feature as cfeature
import netCDF4 as cdf
import json
from datetime import datetime, timedelta

projPC = ccrs.PlateCarree()
lonW = -94
lonE = -83
latS = -4
latN = 4
res = '10m'

fig = plt.figure(figsize=(8, 8.5))
ax = plt.subplot(1, 1, 1, projection=projPC)


ax.set_extent([lonW, lonE, latS, latN], crs=projPC)
ax.coastlines(resolution=res, color='black')
ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='black', linestyle='--')
ax.set_xticks(np.arange(-94, -82.9, 2))
#ax.set_xticklabels(['86°W', '84°W', '82°W', '80°W', '78°W', '76°W', '74°W', '72°W', '70°W', '68°W'])
ax.set_yticks(np.arange(-4, 4.1 , 2))
#ax.set_yticklabels(['22°S', '20°S', '18°S', '16°S', '14°S', '12°S', '10°S', '8°S', '6°S', '4°S', '2°S', '0°N'])


ax.set_title('Áreas seleccionadas para la toma de datos', fontsize= 15)

plt.grid()
plt.show()