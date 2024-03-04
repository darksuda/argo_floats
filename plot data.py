import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

root_folder = "assets/ENC 07032023/" 
file = root_folder + "data.json"
filedata = open(file)
data = json.load(filedata)

#  INDIVIDUAL PLOT
"""
print(len(data))
profileNumber = 4

profile = data[profileNumber]

params = profile['data_info'][0]
param_values = profile['data']

datadf= pd.DataFrame()

for i in [0,2,4]:
    datadf[params[i]] = param_values[i]


id = profile['_id']
platform = str(id[0:-4])
cycle = str(profile['cycle_number'])
lon = profile['geolocation']['coordinates'][0]
lat = profile['geolocation']['coordinates'][1]
date = profile['timestamp'][0:10]

temp_res = [11, 29, 1]
psal_res = [33.9, 35.1, 0.2]
pres_res = [0, 300, 50]



fig, ax = plt.subplots(1,3)

fig.set_figheight(9)
fig.set_figwidth(16)

ax[0].set_xlabel('Temperature (°C)')
ax[0].set_ylabel('Pressure (dbar)')
ax[1].set_xlabel('salinty (psal)')
ax[1].set_ylabel('Pressure (dbar)')
ax[2].set_xlabel('salinty (psal)')
ax[2].set_ylabel('Temperature (°C)')

ax[0].plot(datadf['temperature'], datadf['pressure'])
ax[1].plot(datadf['salinity'], datadf['pressure'])
ax[2].plot(datadf['salinity'], datadf['temperature'])


temp_res.append( int((temp_res[1] - temp_res[0]) / temp_res[2]) + 1)
psal_res.append( int((psal_res[1] - psal_res[0]) / psal_res[2]) + 1)
pres_res.append( int((pres_res[1] - pres_res[0]) / pres_res[2]) + 1)

ax[0].set_xticks(np.linspace(temp_res[0], temp_res[1], temp_res[3]))
ax[1].set_xticks(np.linspace(psal_res[0], psal_res[1], psal_res[3]))
ax[2].set_xticks(np.linspace(psal_res[0], psal_res[1], psal_res[3]))

ax[0].set_yticks(np.linspace(pres_res[0], pres_res[1], pres_res[3]))
ax[1].set_yticks(np.linspace(pres_res[0], pres_res[1], pres_res[3]))
ax[2].set_yticks(np.linspace(temp_res[0], temp_res[1], temp_res[3]))


ax[0].invert_yaxis()
ax[0].set_xbound(temp_res[0], temp_res[1])
ax[0].set_ybound(pres_res[0], pres_res[1])
ax[1].invert_yaxis()
ax[1].set_xbound(psal_res[0],psal_res[1])
ax[1].set_ybound(pres_res[0], pres_res[1])
ax[2].set_xbound(psal_res[0],psal_res[1])
ax[2].set_ybound(temp_res[0], temp_res[1])

ax[0].grid()
ax[1].grid()
ax[2].grid()

plt.suptitle('Platform: '+ str(platform) +'    Cycle: ' + str(cycle) + '\n Date: ' + date + '    Coords: ' + str(np.around(lon, 2)) + ' , ' + str(np.around(lat, 2)))

plt.savefig(root_folder + id + '.jpg')
plt.show()
"""

#  MULTI PLOT COODS in basemap

"""

lons = []
lats = []
ids = []

for i in data:
    lons.append(i['geolocation']['coordinates'][0])
    lats.append(i['geolocation']['coordinates'][1])
    ids.append(i['_id'])

xx, yy = np.meshgrid(lons, lats)

fig = plt.figure(figsize=(16,9))

m = Basemap(projection='merc',
           llcrnrlat = -6, #Lower Left Corner Latitud   SOUTH
           urcrnrlat = -3,  #Upper Right Corner Latitud   NORTH
           llcrnrlon = -85, #Lower Left Corner Longitud   WEAST
           urcrnrlon = -82,  #Upper Right Corner Longitud  EAST
           resolution='h'
           )


m.drawcoastlines()
m.drawmapboundary()
m.fillcontinents(color='coral',lake_color='aqua')

m.drawparallels(np.linspace(-2,-6,5), labels=[True, False, False, False])
m.drawmeridians(np.linspace(-86, -80, 7), labels=[False, False, False, True])


for xy in range(len(lons)):
    m.scatter(lons[xy], lats[xy], latlon=True, label=ids[xy])
    plt.annotate(ids[xy], m(lons[xy], lats[xy]+0.05), fontsize=9)

plt.title('Argo Floats in map - Zoom in')
plt.legend()


plt.show()

"""

