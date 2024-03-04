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
    return (date[8:10] + ' de \n' + months[int(date[5:7])-1]).upper()

projPC = ccrs.PlateCarree()
lonW = -90
lonE = -68
latS = -22
latN = 2
res = '10m'

cdf_file = 'assets\COPERNICUS_DWNLDS\PSAL_COP_DIC_2023_PERU.nc'
cdf_data = cdf.Dataset(cdf_file)

counter = 0

for i in range(len(cdf_data['time'])):
    temp = np.array(cdf_data['so'])[i][0]
    lat = np.array(cdf_data['latitude'])
    lon = np.array(cdf_data['longitude'])
    time = str(datetime(1950,1,1) + timedelta(hours= float(cdf_data['time'][i])))
    fig = plt.figure(figsize=(8, 8.5))
    ax = plt.subplot(1, 1, 1, projection=projPC)


    ax.set_extent([lonW, lonE, latS, latN], crs=projPC)
    ax.coastlines(resolution=res, color='black')
    ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='black', linestyle='--')
    ax.set_xticks(np.arange(-90, -68 +1, 2))
    ax.set_xticklabels(['90°W','88°W','86°W', '84°W', '82°W', '80°W', '78°W', '76°W', '74°W', '72°W', '70°W', '68°W'])
    ax.set_yticks(np.arange(-22, 2 + 1 , 2))
    ax.set_yticklabels(['22°S', '20°S', '18°S', '16°S', '14°S', '12°S', '10°S', '8°S', '6°S', '4°S', '2°S', '0°N', '2°N'])

    plt.title('SALINIDAD SUPERFICIAL DEL MAR\n' + set_date(time))
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.grid()

    cmap = mpl.colors.ListedColormap(['#FF0000', '#FF00FF', '#00FFFF', '#FFFF00'])
    bounds = [30, 33.8, 34.8, 35.1, 37]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)


    plot_tsm = ax.contourf(lon, lat, temp, levels = np.linspace(32, 37, 101), cmap = cmap, norm= norm, alpha=0.75)
    plot_tsm_lines = ax.contour(plot_tsm, levels=np.arange(32, 37.0, 0.2), colors = '#c70626', linewidths= 0.2, linestyles = 'solid')
    plot_tsm_lines_x = ax.contour(plot_tsm, levels=[33.8, 34.8, 35.1], colors = 'black', linewidths= 0.8, linestyles = 'solid')
    ax.contour(plot_tsm, levels=[33.8, 34.8, 35.1], colors = 'black', linewidths= 0.5, linestyles = 'dashed')
    #ax.clabel(plot_tsm_lines_x, levels=[33.8, 34.8, 35.1] ,inline=True, fontsize=7.5, colors = 'black')
    ax.text(-74, -9.5, set_date_2(time) + ' DEL 2023', fontsize=18, horizontalalignment='center')

    cbar = plt.colorbar(plot_tsm)
    cbar.set_label('Salinidad (psu)')
    cbar.set_ticks([32, 33.8, 34.8, 35.1, 37])

    ax.set_extent([-86 , -68, 0, -22], crs=ccrs.PlateCarree())

    #plt.show()
    #break

    plt.savefig('IMGS/PSAL/PSAL_COP_'+ str(counter)+ '_PERU_SEP_DIC')
    plt.close()
    counter += 1

    print('imagen '+ str(i)+ ' creada...')

