import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import gsw

psal_start  = 34.8
psal_end = 35.6

temp_start = 10
temp_end = 28

pres_start = 0
pres_end = 300

floats_list_1 = ['6903000_102', '6903002_102','6903003_102']
floats_list_2 = ['6903000_103', '6903002_103','6903003_103']
"""
floats_list_1 = ['6902962_069']
floats_list_2 = ['6902962_070']"""

for i in range(len((floats_list_2))):

    file_1 = open('assets\ARGOS_DWNLDS\INDIVIDUAL/'+ floats_list_1[i] + '.json')
    data_1 = json.load(file_1)

    file_2 = open('assets\ARGOS_DWNLDS\INDIVIDUAL/'+ floats_list_2[i] + '.json')
    data_2 = json.load(file_2)



    for i in range(len(data_2)):
        id = data_1[i]['_id']
        platform = str(id[0:-4])
        lon = data_1[i]['geolocation']['coordinates'][0]
        lat = data_1[i]['geolocation']['coordinates'][1]
        date = data_1[i]['timestamp'][0:10]
        cycle = str(data_1[i]['cycle_number'])
        params = data_1[i]['data_info'][0]
        param_values = data_1[i]['data']
        index_CTD = []

        id_2 = data_2[i]['_id']
        platform_2 = str(id[0:-4])
        lon_2 = data_2[i]['geolocation']['coordinates'][0]
        lat_2 = data_2[i]['geolocation']['coordinates'][1]
        date_2 = data_2[i]['timestamp'][0:10]
        cycle_2 = str(data_2[i]['cycle_number'])
        params_2 = data_2[i]['data_info'][0]
        param_values_2 = data_2[i]['data']
        index_CTD_2 = []

        index_CTD.append(params.index('salinity_sfile')) if 'salinity_sfile' in params else index_CTD.append(params.index('salinity'))
        index_CTD.append(params.index('temperature_sfile')) if 'temperature_sfile' in params else index_CTD.append(params.index('temperature'))
        index_CTD.append(params.index('pressure'))
        if 'doxy' in params:
            index_CTD.append(params.index('doxy')) 
        datadf= pd.DataFrame()
        for i in index_CTD:
            datadf[params[i]] = param_values[i]

        psal = datadf.columns[0]
        temp = datadf.columns[1]
        pres = datadf.columns[2]
        if 'doxy' in params:
            doxy = datadf.columns[3]


        index_CTD_2.append(params_2.index('salinity_sfile')) if 'salinity_sfile' in params_2 else index_CTD_2.append(params_2.index('salinity'))
        index_CTD_2.append(params_2.index('temperature_sfile')) if 'temperature_sfile' in params_2 else index_CTD_2.append(params_2.index('temperature'))
        index_CTD_2.append(params_2.index('pressure'))
        if 'doxy' in params_2:
            index_CTD_2.append(params_2.index('doxy')) 
        datadf_2= pd.DataFrame()
        for i in index_CTD_2:
            datadf_2[params_2[i]] = param_values_2[i]

        psal = datadf.columns[0]
        temp = datadf.columns[1]
        pres = datadf.columns[2]
        if 'doxy' in params:
            doxy = datadf.columns[3]

        psal_2 = datadf_2.columns[0]
        temp_2 = datadf_2.columns[1]
        pres_2 = datadf_2.columns[2]
        if 'doxy' in params_2:
            doxy_2 = datadf_2.columns[3]

        mint=np.min(datadf[temp])
        maxt=np.max(datadf[temp])

        mins=np.min(datadf[psal])
        maxs=np.max(datadf[psal])

        tempL=np.linspace(temp_start ,temp_end ,50)
        salL=np.linspace(psal_start ,psal_end ,50)

        Tg, Sg = np.meshgrid(tempL,salL)
        sigma_theta = gsw.sigma0(Sg, Tg)

        fig, ax = plt.subplots(1,3, figsize = (16,9))
        ax[0].plot(datadf[temp], datadf[pres] , label= date[-2:] + ' DE AGOSTO', color='red')
        ax[0].plot(datadf_2[temp_2], datadf_2[pres_2] , label= date_2[-2:] + '  DE SEPTIEMBRE', color='blue')
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
        ax[0].legend()

        ax[1].plot(datadf[psal], datadf[pres] , label= date[-2:] + ' DE AGOSTO', color='red')
        ax[1].plot(datadf_2[psal_2], datadf_2[pres_2] , label= date_2[-2:] + '  DE SEPTIEMBRE', color='blue')
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
        ax[1].legend()

        ax[2].plot(datadf[psal], datadf[temp] , label= date[-2:] + ' DE AGOSTO', color='red')
        ax[2].plot(datadf_2[psal_2], datadf_2[temp_2] , label= date_2[-2:] + '  DE SEPTIEMBRE', color='blue')
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
        ax[2].legend()

        plt.suptitle('Platform: '+ str(platform_2) +'   Cycle: '+ str(cycle) + '-' + str(cycle_2) + '\n Date: ' + date_2 + '   Coords: ' + str(np.round(lon_2, 2)) + ' , ' + str(np.round(lat_2, 2)) )
        plt.figtext(0.08, 0.02, "Fuente: Argo (https://argo.ucsd.edu)", fontsize=6.5)
        

        #plt.savefig('IMGS/COMPARE/profile'+id+'_SEP')
        plt.show()
        #plt.close()#

        if 'doxy' in params:
            fig2, ax2 = plt.subplots(figsize = (12,7))
            ax2.set_xticks(np.linspace(0, 300, 17), list(map(lambda x: x * 0.032 , np.linspace(0, 300, 17))))
            ax2.scatter(datadf[doxy], datadf[pres], s=9, label = date)
            ax2.scatter(datadf_2[doxy_2], datadf_2[pres_2], s=9, label = date_2)
            ax2.invert_yaxis()
            ax2.set_title('Platform: '+ str(platform_2) +'   Cycle: ' + str(cycle) + '-' + str(cycle_2) + '\n Date: ' + date_2 + '   Coords: ' + str(np.round(lon_2, 2)) + ' , ' + str(np.round(lat_2, 2)) + '\nOxígeno disuelto')
            ax2.set_xlabel('Oxígeno disuelto (mgO2/Kg)')
            ax2.set_ylabel('Presión (dbar)')
            ax2.set_yticks(np.linspace(0,300,13))
            ax2.set_ybound(pres_start, pres_end)
            ax2.grid()

            #plt.savefig('IMGS/profile_doxy_'+id+'_SEP')
            plt.show()
            #plt.close()

