import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import gsw


floats_list_1 = ['6903000_081', '6903002_081','6903003_081']
floats_list_2 = ['6903000_082', '6903002_082','6903003_082']

for i in range(len((floats_list_2))):

    file_1 = open('assets\ARGOS_DWNLDS\INDIVIDUAL/'+ floats_list_1[i] + '.json')
    data_1 = json.load(file_1)

    file_2 = open('assets\ARGOS_DWNLDS\INDIVIDUAL/'+ floats_list_2[i] + '.json')
    data_2 = json.load(file_2)

    psal_start  = 33.9
    psal_end = 35.6

    temp_start = 10
    temp_end = 30

    pres_start = 0
    pres_end = 300

fig, ax = plt.subplots(1,3, figsize = (16,9))

for i in range(len(data_2)):
    id_2 = data_2[i]['_id']
    id_1 = data_1[i]['_id']
    platform_2 = str(id_2[0:-4])
    platform_1 = str(id_1[0:-4])
    lon_2 = data_2[i]['geolocation']['coordinates'][0]
    lon_1 = data_2[i]['geolocation']['coordinates'][0]
    lat_2 = data_2[i]['geolocation']['coordinates'][1]
    lat_1 = data_1[i]['geolocation']['coordinates'][1]
    date_2 = data_2[i]['timestamp'][0:10]
    date_1 = data_1[i]['timestamp'][0:10]
    cycle_2 = str(data_2[i]['cycle_number'])
    cycle_1 = str(data_1[i]['cycle_number'])
    params_2 = data_2[i]['data_info'][0]
    params_1 = data_1[i]['data_info'][0]
    param_values_2 = data_2[i]['data']
    param_values_1 = data_1[i]['data']
    index_CTD_2 = []
    index_CTD_1 = []

    index_CTD_2.append(params_2.index('salinity_sfile')) if 'salinity_sfile' in params_2 else index_CTD_2.append(params_2.index('salinity'))
    index_CTD_2.append(params_2.index('temperature_sfile')) if 'temperature_sfile' in params_2 else index_CTD_2.append(params_2.index('temperature'))
    index_CTD_2.append(params_2.index('pressure'))
    if 'doxy' in params_2:
        index_CTD_2.append(params_2.index('doxy')) 

    index_CTD_1.append(params_1.index('salinity_sfile')) if 'salinity_sfile' in params_1 else index_CTD_1.append(params_1.index('salinity'))
    index_CTD_1.append(params_1.index('temperature_sfile')) if 'temperature_sfile' in params_1 else index_CTD_1.append(params_1.index('temperature'))
    index_CTD_1.append(params_1.index('pressure'))
    if 'doxy' in params_1:
        index_CTD_1.append(params_1.index('doxy')) 


    datadf_2= pd.DataFrame()
    for i in index_CTD_2:
        datadf_2[params_2[i]] = param_values_2[i]
    psal_2 = datadf_2.columns[0]
    temp_2 = datadf_2.columns[1]
    pres_2 = datadf_2.columns[2]
    if 'doxy' in params_2:
        doxy_2 = datadf_2.columns[3]


    datadf_1= pd.DataFrame()
    for i in index_CTD_1:
        datadf_1[params_1[i]] = param_values_1[i]
    psal_1 = datadf_1.columns[0]
    temp_1 = datadf_1.columns[1]
    pres_1 = datadf_1.columns[2]
    if 'doxy' in params_1:
        doxy_1 = datadf_1.columns[3]

    mint=np.min(datadf_2[temp_2])
    maxt=np.max(datadf_2[temp_2])

    mins=np.min(datadf_2[psal_2])
    maxs=np.max(datadf_2[psal_2])

    tempL=np.linspace(temp_start ,temp_end ,50)
    salL=np.linspace(psal_start ,psal_end ,50)

    Tg, Sg = np.meshgrid(tempL,salL)
    sigma_theta = gsw.sigma0(Sg, Tg)


ax[0].plot(datadf_1[temp_1], datadf_1[pres_1])
ax[0].plot(datadf_2[temp_2], datadf_2[pres_2])
ax[0].axhline(y=25, color="#c3093f")
ax[0].invert_yaxis()
ax[0].set_xticks(np.linspace(10,30,11))
ax[0].set_yticks(np.linspace(0,300,13))
ax[0].set_ybound(pres_start, pres_end)
ax[0].set_xbound(temp_start, temp_end)
ax[0].set_title('Temperatura vs Presión')
ax[0].set_xlabel('Temperatura (°C)')
ax[0].set_ylabel('Presión (dbar)')
ax[0].grid()

ax[1].plot(datadf_2[psal_2], datadf_2[pres_2])
ax[1].axhline(y=25, color="#c3093f")
ax[1].axvline(x=35.1, color="#c3093f")
ax[1].axvline(x=34.8, color="#c3093f")
ax[1].axvline(x=33.8, color="#c3093f")
ax[1].invert_yaxis()
ax[1].set_xticks(np.linspace(33.3, 36.3, 16))
ax[1].set_yticks(np.linspace(0,300,13))
ax[1].set_ybound(pres_start, pres_end)
ax[1].set_xbound(psal_start, psal_end)
ax[1].set_title('Salinidad vs Presión')
ax[1].set_xlabel('Salinidad (psu)')
ax[1].set_ylabel('Presión (dbar)')
ax[1].grid()

ax[2].plot(datadf_2[psal_2], datadf_2[temp_2])
plot_ts = ax[2].contour(Sg, Tg, sigma_theta, colors='grey', zorder=1)
cl=plt.clabel(plot_ts,fontsize=10,inline=True)
ax[2].set_xticks(np.linspace(33.3, 36.3, 16))
ax[2].set_yticks(np.linspace(10,30,11))
ax[2].set_ybound(temp_start, temp_end)
ax[2].set_xbound(psal_start, psal_end)
ax[2].set_title('Diagrama TS')
ax[2].set_xlabel('Salinidad (psu)')
ax[2].set_ylabel('Temperatura (°C)')
ax[2].grid()

plt.suptitle('Platform: '+ str(platform_2) +'   Cycle: ' + str(cycle_1) + ' - '+ str(cycle_2) + '\n Date: ' + date_2 + '   Coords: ' + str(np.round(lon_2, 2)) + ' , ' + str(np.round(lat_2, 2)) )
plt.figtext(0.08, 0.02, "Fuente: Argo (https://argo.ucsd.edu)", fontsize=6.5)


#plt.savefig('IMGS/profile'+id+'_25_02_apr')
plt.show()
plt.close()

