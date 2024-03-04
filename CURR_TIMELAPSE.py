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
lonW = -86
lonE = -68
latS = -22
latN = 0
res = '10m'

cdf_file = 'assets\COPERNICUS_DWNLDS\CUR_COP_01_ENE_27_JUN.nc'
cdf_data = cdf.Dataset(cdf_file)
counter = 59

for i in range(157):
    vo = np.array(cdf_data['vo'])[i][0]
    vo[vo == 9.96921e+36] = np.NaN
    uo = np.array(cdf_data['uo'])[i][0]
    uo[uo == 9.96921e+36] = np.NaN
    cv = np.array(((vo**2) + (uo**2))**0.5)
    lat = np.array(cdf_data['latitude'])
    lon = np.array(cdf_data['longitude'])
    time = str(datetime(1950,1,1) + timedelta(hours= float(cdf_data['time'][i])))
    fig = plt.figure(figsize=(10, 12))
    ax = plt.subplot(1, 1, 1, projection=projPC)


    ax.set_extent([lonW, lonE, latS, latN], crs=projPC)
    ax.coastlines(resolution=res, color='black')
    ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='green', linestyle='--')
    ax.set_xticks(np.linspace(-86, -68, 10))
    ax.set_xticklabels(['86°W', '84°W', '82°W', '80°W', '78°W', '76°W', '74°W', '72°W', '70°W', '68°W'])
    ax.set_yticks(np.linspace(-20, 0 , 11))
    ax.set_yticklabels(['20°S', '18°S', '16°S', '14°S','12°S', '10°S', '8°S', '6°S', '4°S', '2°S', '0°N'])
    ax.text(-70, -17.5, set_date_2(time), fontsize=18, horizontalalignment='center')

    plt.title('CORRIENTE SUPERFICIAL DEL MAR\n' +  set_date(time))
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.grid()

    plot_tsm = ax.contourf(lon, lat, cv, cmap = 'rainbow')
    ax.quiver(x=lon, y=lat, u=uo, v=vo)
    plot_tsm_lines = ax.contour(plot_tsm, levels=np.arange(15, 30), colors = 'black', linewidths= 0.2, linestyles = 'solid')
    ax.clabel(plot_tsm_lines, levels=np.arange(15, 30) ,inline=True, fontsize=7.5, colors = 'black')

    cbar = plt.colorbar(plot_tsm)
    cbar.set_label('Velocidad (m/s)')

    plt.tight_layout()
    plt.show()
    break

    #plt.savefig('IMGS/CUR/CUR_COP_PERU'+ str(counter)+'_3')
    #plt.close()
    counter += 1

    print('imagen '+ str(i)+ ' creada...')