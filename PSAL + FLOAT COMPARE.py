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

cdf_file = 'assets\COPERNICUS_DWNLDS\PSAL_COP_OCT_03_PERU.nc'
cdf_data = cdf.Dataset(cdf_file)

temp = np.array(cdf_data['so'])[0][0]
lat = np.array(cdf_data['latitude'])
lon = np.array(cdf_data['longitude'])

floats_list_1 = ['6903000_072', '6903002_072','6903003_072']
floats_list_2 = ['6903000_108', '6903002_108','6903003_108']

floatsdf_1 = []
for fl in floats_list_1:
    floatsdf_1.append(json.load(open('assets/ARGOS_DWNLDS/INDIVIDUAL/'+fl + '.json'))[0])

floatsdf_2 = []
for fl in floats_list_2:
    floatsdf_2.append(json.load(open('assets/ARGOS_DWNLDS/INDIVIDUAL/'+fl + '.json'))[0])

lats_1 = []
lons_1 = []
dates_1 = []

for i in floatsdf_1:
        lons_1.append(i['geolocation']['coordinates'][0])
        lats_1.append(i['geolocation']['coordinates'][1])
        dates_1.append(i['timestamp'][0:10])

lats_2 = []
lons_2 = []
dates_2 = []

for i in floatsdf_2:
        lons_2.append(i['geolocation']['coordinates'][0])
        lats_2.append(i['geolocation']['coordinates'][1])
        dates_2.append(i['timestamp'][0:10])



fig = plt.figure(figsize=(8, 8.5))
ax = plt.subplot(1, 1, 1, projection=projPC)


ax.set_extent([lonW, lonE, latS, latN], crs=projPC)
ax.coastlines(resolution=res, color='black')
ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='green', linestyle='--')
ax.set_xticks(np.linspace(-86, -68, 10))
ax.set_xticklabels(['86°W', '84°W', '82°W', '80°W', '78°W', '76°W', '74°W', '72°W', '70°W', '68°W'])
ax.set_yticks(np.linspace(-22, 0 , 12))
ax.set_yticklabels(['22°S', '20°S', '18°S', '16°S', '14°S', '12°S', '10°S', '8°S', '6°S', '4°S', '2°S', '0°N'])

ax.set_extent([-86 , -68, 0, -22], crs=ccrs.PlateCarree())

plt.title('SALINIDAD SUPERFICIAL DEL MAR\n03 OCTUBRE 2023')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.grid()




cmap = mpl.colors.ListedColormap(['#FF0000', '#FF00FF', '#00FFFF', '#FFFF00'])
bounds = [32, 33.8, 34.8, 35.1, 37]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)


plot_tsm = ax.contourf(lon, lat, temp, levels = np.linspace(32, 37, 101), cmap = cmap, norm= norm, alpha=0.75)
plot_tsm_lines = ax.contour(plot_tsm, levels=np.arange(32, 37.0, 0.2), colors = '#c70626', linewidths= 0.2, linestyles = 'solid')
plot_tsm_lines_x = ax.contour(plot_tsm, levels=[33.8, 34.8, 35.1], colors = 'black', linewidths= 0.8, linestyles = 'solid')
ax.contour(plot_tsm, levels=[33.8, 34.8, 35.1], colors = 'black', linewidths= 0.5, linestyles = 'dashed')
ax.clabel(plot_tsm_lines_x, levels=[33.8, 34.8, 35.1] ,inline=True, fontsize=7.5, colors = 'black')

cbar = plt.colorbar(plot_tsm)
cbar.set_label('Salinidad (psu)')
cbar.set_ticks([32, 33.8, 34.8, 35.1, 37])

#floats_1 = ax.scatter(lons_1, lats_1, s=80, color='red', edgecolors="#000a2e", label='Argo floats antes')
floats_2 = ax.scatter(lons_2, lats_2, s=80, color='blue', edgecolors="#000a2e", label='Argo floats ahora')

#plt.legend(loc='center left', bbox_to_anchor=(0.8, -0.08))


"""fig_manager = plt.get_current_fig_manager()
fig_manager.window.showMaximized()"""
plt.show()