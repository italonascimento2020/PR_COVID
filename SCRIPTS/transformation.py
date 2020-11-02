import pandas as pd
import json
import time
from APP import api_connection as api

def GetAllCountries(**dict):
    
    dict.update({ 'url': "https://covid-19-data.p.rapidapi.com/help/countries"})
    dict.update({ 'querystring': {"format":"json"}})

    getListOfCountries = api.get_response(**dict)
     
    return normalize_js(getListOfCountries)

def GetListByCountryName(**dict):
    
    dict.update({ 'url': "https://covid-19-data.p.rapidapi.com/country"})
    
    DfListOfNames = dict.get("ListOfCountries")
    timer = int(dict.get("timer"))

    DfList = []

    for key, row in DfListOfNames.iterrows():
        
        dict.update({ 'querystring': {"format":"json","name":row['name']}})
        
        time.sleep(timer)
        
        getAllOfEachCountry = api.get_response(**dict)

        df = normalize_js(getAllOfEachCountry)

        DfList.append(df)
        
    result_df = pd.concat(DfList)

    return result_df

def normalize_js(js):
 
    data = json.loads(js.text) 

    return pd.json_normalize(data)
