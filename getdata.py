import netCDF4 as cdf
import numpy as np
import matplotlib.pyplot as plt

data = cdf.Dataset('SD6902963_031.nc')

variables_names = []
for i in data.variables.keys():
    variables_names.append(i)

print(variables_names)

temp = np.array(data['TEMP'][0])
temp_A = np.array(data['TEMP_ADJUSTED'][0])
psal = np.array(data['PSAL'][0])
psal_A = np.array(data['PSAL_ADJUSTED'][0])
pres = np.array(data['PRES'][0])
pres_A = np.array(data['PRES_ADJUSTED'][0])


for i in range(50):
    print(np.array(data['TEMP_ADJUSTED_QC'])[0][i], np.array(data['TEMP_QC'])[0][i], np.array(data['TEMP'])[0][i], np.array(data['TEMP_ADJUSTED'])[0][i])
    print('------------')

"""
fig, ax = plt.subplots(1,2)
ax[0].scatter(temp, pres, color='red')
ax[0].scatter(temp_A, pres_A, color='black')
ax[1].scatter(psal, pres, color='red')
ax[1].scatter(psal_A, pres_A, color='black')

ax[0].invert_yaxis()
ax[1].invert_yaxis()
ax[0].set_ybound(0,50)
ax[1].set_ybound(0,50)
ax[0].set_xbound(10,30)
ax[1].set_xbound(34,36)


plt.show()

"""