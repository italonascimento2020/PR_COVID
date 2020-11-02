import json

from APP import api_connection as api
from SCRIPTS import transformation as tr

CONFIG_FILE_NAME = "config.json" 

def main(): 
 
    with open(CONFIG_FILE_NAME) as config_file:
        config_filedata = json.load(config_file)
    
    host = config_filedata['host']
    key = config_filedata['key']
    timer = config_filedata['timer']

    dict = {}

    dict.update({ 'host': host})
    dict.update({ 'key': key})
    dict.update({ 'timer': timer})
    #getListOfCountries 
    
    all_countries_name = tr.GetAllCountries(**dict)

    dict.update({'ListOfCountries': all_countries_name})

    df = tr.GetListByCountryName(**dict)
    
    df.to_csv('result.csv')

if __name__ == "__main__":
    main()