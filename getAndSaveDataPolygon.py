import json
import pandas as pd
from argovisHelpers import helpers as avh

API_KEY='7f8d3cf6ecbf39891eca1273dda99216809e8fa0' #crear cuenta en ARGOVIS 
API_PREFIX = 'https://argovis-api.colorado.edu/'   #https://argovis-keygen.colorado.edu


polygon = '[[-86,0],[-68,0],[-68,-20],[-86,-20],[-86,0]]'  #AREA PERU
#polygon = '[[-180,-3],[-175,-3],[-175,-7],[-180,-7],[-180,-3]]'   #AREA PERSONALIZADA

params = {
        'startDate': '2024-02-20T00:00:00Z',
        'endDate': '2024-02-26T00:00:00Z',
        'source': 'argo_core',                         # argo_core , argo_deep, argo_bgc
        'polygon': polygon,
        'data': 'all'
    }

d = avh.query('argo', options=params, apikey=API_KEY, apiroot=API_PREFIX)

#data = open('data_nov_2015_A.json', 'w')
data = open('data.json', 'w')
data.write(json.dumps(d))
data.close()
