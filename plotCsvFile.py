import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

root_folder = "assets/ENC 07032023/" 
file = root_folder + "dataCTD_6903002_064.csv"
meta = root_folder + "metaCTD_6903002_064.csv"

datadf = pd.read_csv(file)
metadf = pd.read_csv(meta)

id = metadf['id'][0]
platform = metadf['platform'][0]
cycle = metadf['cycle'][0]
lon = metadf['lon'][0]
lat = metadf['lat'][0]
date = metadf['date'][0]



fig, ax = plt.subplots(1,3)

ax[0].set_xlabel('Temperature (°C)')
ax[0].set_ylabel('Pressure (dbar)')
ax[1].set_xlabel('salinty (psal)')
ax[1].set_ylabel('Pressure (dbar)')
ax[2].set_xlabel('salinty (psal)')
ax[2].set_ylabel('Temperature (°C)')

ax[0].plot(datadf['temperature'], datadf['pressure'])
ax[1].plot(datadf['salinity'], datadf['pressure'])
ax[2].plot(datadf['salinity'], datadf['temperature'])

temp_res = [12, 28, 1]
psal_res = [34.3, 35.1, 0.2]
pres_res = [0, 300, 50]

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

plt.suptitle('Platform: '+ str(platform) +' Cycle: ' + str(cycle) + '\n Date: ' + date + ' Coords: ' + str(lon) + ' , ' + str(lat) )

plt.show()
