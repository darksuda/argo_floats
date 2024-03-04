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

cdf_file = 'assets/COPERNICUS_DWNLDS/TSM_COP_NOV_09_PERU.nc'
cdf_data = cdf.Dataset(cdf_file)

counter = 0

for i in range(len(np.array(cdf_data['thetao']))):
    temp = np.array(cdf_data['thetao'])[i][0]
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
    ax.text(-74, -9.5, set_date_2(time) + ' DEL 2023', fontsize=18, horizontalalignment='center')

    plt.title('TEMPERATURA SUPERFICIAL DEL MAR\n' +  set_date(time))
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.grid()

    plot_tsm = ax.contourf(lon, lat, temp, levels = np.linspace(13, 31, 19), cmap = 'rainbow')
    plot_tsm_lines = ax.contour(plot_tsm, levels=np.arange(15, 30), colors = 'black', linewidths= 0.2, linestyles = 'solid')
    #ax.contour(plot_tsm, levels=[29, 27, 25, 23, 21, 19], colors = 'black', linewidths= 0.5, linestyles = 'dashed')
    ax.clabel(plot_tsm_lines, levels=np.arange(15, 30) ,inline=True, fontsize=7.5, colors = 'black')

    cbar = plt.colorbar(plot_tsm)
    cbar.set_label('Temperatura (°C)')

    ax.set_extent([-90 , -68, 2, -22], crs=ccrs.PlateCarree())
    
    #floats_1 = ax.scatter(lons_1, lats_1, s=30, color='#ffff00', edgecolors="#000a2e", label='Argo floats antes')
    #floats_2 = ax.scatter(lons_2, lats_2, s=30, color='#02e60e', edgecolors="#000a2e", label='Argo floats ahora')

    plt.show()
    break

    plt.savefig('IMGS/TSM/TSM_COP_'+ str(counter) + '_PERU_ENE_OCT')
    plt.close()
    counter += 1

    print('imagen '+ str(i)+ ' creada...')