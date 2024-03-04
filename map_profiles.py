import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from cartopy import crs as ccrs, feature as cfeature
import netCDF4 as cdf
import json

projPC = ccrs.PlateCarree()
lonW = -86
lonE = -68
latS = -22
latN = 0
res = '10m'


floatsdf = json.load(open('data.json'))

lats = []
lons = []
dates = []
ids = []

for i in floatsdf:
        lons.append(i['geolocation']['coordinates'][0])
        lats.append(i['geolocation']['coordinates'][1])
        dates.append(i['timestamp'][0:10])
        ids.append(i['_id'])



fig = plt.figure(figsize=(8, 8.5))
ax = plt.subplot(1, 1, 1, projection=projPC)


ax.set_extent([lonW, lonE, latS, latN], crs=projPC)
ax.coastlines(resolution=res, color='black')
ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='green', linestyle='--')
ax.set_xticks(np.linspace(-86, -68, 10))
ax.set_xticklabels(['86°W', '84°W', '82°W', '80°W', '78°W', '76°W', '74°W', '72°W', '70°W', '68°W'])
ax.set_yticks(np.linspace(-22, 0 , 12))
ax.set_yticklabels(['22°S', '20°S', '18°S', '16°S', '14°S', '12°S', '10°S', '8°S', '6°S', '4°S', '2°S', '0°N'])

ax.set_extent([-86 , -68, 0, -20], crs=ccrs.PlateCarree())

counter = 0
ax.scatter(lons, lats, color= 'yellow', edgecolor='black')
for i in range(len(ids)):
    ax.text(lons[i] ,lats[i]+0.15, str(counter))
    counter += 1


plt.title('Argo floats february 2024')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid()


plt.show()