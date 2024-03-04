from argovisHelpers import helpers as avh
import json
import requests


API_ROOT='https://argovis-api.colorado.edu/'
API_KEY='7f8d3cf6ecbf39891eca1273dda99216809e8fa0'

floats_list_1 = ['6903000_107', '6903002_107','6903003_107']
floats_list_2 = ['6903000_115', '6903002_114','6903003_114']

platform_id ='6903002_115'

dataQuery = {
    'cycle': platform_id,
    'data': 'all'
}

d = avh.query('argo', options=dataQuery, apikey=API_KEY, apiroot=API_ROOT)

data = open('assets/ARGOS_DWNLDS/INDIVIDUAL/'+ platform_id +'.json', 'w')
data.write(json.dumps(d))
data.close()
