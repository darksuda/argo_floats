import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from cartopy import crs as ccrs, feature as cfeature
import netCDF4 as cdf
import json
from datetime import datetime, timedelta

def set_date(date):
    months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    return (date[8:10] + ' de ' + months[int(date[5:7])-1]).upper()

def set_date_2(date):
    months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    #return (date[8:10] + ' de \n' + months[int(date[5:7])-1]).upper()
    return (months[int(date[5:7])-1]).upper()

def set_date_3(date):
    months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    return (months[int(date[5:7])-1] + '\n' + date[:4]).upper()

projPC = ccrs.PlateCarree()
lonW = -90
lonE = -68
latS = -22
latN = 2
res = '10m'

cdf_file = 'assets\COPERNICUS_DWNLDS\SSH_COP_ENE_2024_PERU_M.nc'
cdf_data = cdf.Dataset(cdf_file)

so = np.array(cdf_data['zos'])
lat = np.array(cdf_data['latitude'])
lon = np.array(cdf_data['longitude'])
time = str(datetime(1950,1,1) + timedelta(hours= float(cdf_data['time'][0])))

data = []

for i in so:
    data.append(i)

data = np.array(data)
data = np.mean(data, axis =0)

fig = plt.figure(figsize=(8, 8.5))
ax = plt.subplot(1, 1, 1, projection=projPC)

ax.set_extent([lonW, lonE, latS, latN], crs=projPC)
ax.coastlines(resolution=res, color='black')
ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='green', linestyle='--')
ax.set_xticks(np.arange(-90, -68 +1, 2))
ax.set_xticklabels(['90°W','88°W','86°W', '84°W', '82°W', '80°W', '78°W', '76°W', '74°W', '72°W', '70°W', '68°W'], fontsize=8)
ax.set_yticks(np.arange(-22, 20 + 1 , 2))
ax.set_yticklabels(['22°S', '20°S', '18°S', '16°S', '14°S', '12°S', '10°S', '8°S', '6°S', '4°S', '2°S', '0°N', '2°N', '4°N', '6°N', '8°N', '10°N', '12°N', '14°N', '16°N', '18°N', '20°N'], fontsize=8)
ax.text(-74, -0, set_date_3(time), fontsize=18, horizontalalignment='center')

ax.set_extent([-90 , -68, 20, -20], crs=ccrs.PlateCarree())

plt.title('ALTURA DINÁMICA DEL MAR\n' +  set_date_2(time) )
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.grid()




plot_tsm = ax.contourf(lon, lat, data, levels=np.linspace(-.6,.6, 25) , cmap = 'coolwarm')
plot_tsm_lines = ax.contour(plot_tsm, levels=np.linspace(-.6,.6, 25), colors = 'black', linewidths= 0.2, linestyles = 'solid')
ax.contour(plot_tsm, levels=[0.1], colors = 'black', linewidths= 1.3, linestyles = 'dotted')
ax.contour(plot_tsm, levels=[0.2], colors = 'black', linewidths= 1.3, linestyles = 'solid')
#ax.contour(plot_tsm, levels=[29, 27, 25, 23, 21, 19], colors = 'black', linewidths= 0.5, linestyles = 'dashed')
ax.clabel(plot_tsm_lines, levels=np.linspace(-.6,.6, 13) ,inline=True, fontsize=7.5, colors = 'black')

plt.figtext(0.25, 0.02, "Fuente: Copernicus Marine Service - GOPAF\n(https://doi.org/10.48670/moi-00016)", fontsize=6.5)
plt.figtext(0.75, 0.02, "Por: Carlo Ilave", fontsize=6.5, family ='serif')

cbar = plt.colorbar(plot_tsm)
cbar.set_label('Altura dinámica (m)')


plt.show()