import matplotlib.pyplot as plt
import numpy as np
from cartopy import crs as ccrs, feature as cfeature
import netCDF4 as cdf
import json

projPC = ccrs.PlateCarree()
lonW = -90
lonE = -80
latS = -10
latN = 0
res = '10m'

cdf_file = 'assets\COPERNICUS_DWNLDS/area_n_16.05.2023.nc'
cdf_data = cdf.Dataset(cdf_file)

temp = np.array(cdf_data['thetao'])[0][0]
print(temp.max())
lat = np.array(cdf_data['latitude'])
lon = np.array(cdf_data['longitude'])

fig = plt.figure(figsize=(11, 8.5))
ax = plt.subplot(1, 1, 1, projection=projPC)


ax.set_extent([lonW, lonE, latS, latN], crs=projPC)
ax.coastlines(resolution=res, color='black')
ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='green', linestyle='--')
#ax.set_xticks(np.linspace(-86, -68, 10))
#ax.set_xticklabels(['86°W', '84°W', '82°W', '80°W', '78°W', '76°W', '74°W', '72°W', '70°W', '68°W'])
#ax.set_yticks(np.linspace(-22, 0 , 12))
#ax.set_yticklabels(['22°S', '20°S', '18°S', '16°S', '14°S', '12°S', '10°S', '8°S', '6°S', '4°S', '2°S', '0°N'])

plt.title('Argo Floats en la costa peruana\n16/05/2023')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.grid()

plot_tsm = ax.contourf(lon, lat, temp, levels = np.linspace(13, 31, 19), cmap = 'rainbow')
plot_tsm_lines = ax.contour(plot_tsm, levels=np.arange(15, 30), colors = 'black', linewidths= 0.2, linestyles = 'solid')
#ax.contour(plot_tsm, levels=[29, 27, 25, 23, 21, 19], colors = 'black', linewidths= 0.5, linestyles = 'dashed')
ax.clabel(plot_tsm_lines, levels=np.arange(15, 30) ,inline=True, fontsize=7.5, colors = 'black')

plt.colorbar(plot_tsm)


fig_manager = plt.get_current_fig_manager()
fig_manager.window.showMaximized()
plt.show()
