import requests
from requests import Response
import sqlite3

def get_sitenames()->list[str]:
    url='https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON'
    try:
        res:Response = requests.get(url)
        res.raise_for_status()
        data=res.json()
    except Exception as e:
        print(e)
    else:
        sitenames =set()
        for items in data['records']:
            sitenames.add(items['sitename'])

        sitenames = list(sitenames)
        return sitenames
    


def get_selected_data(sitename:str)->list[list]:
    url='https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON'
    try:
        res:Response = requests.get(url)
        res.raise_for_status()
        data=res.json()
    except Exception as e:
        print(e)
    else:
        outerlist = []

        for items in data['records']:
            if items['sitename'] == sitename:
                innerlist = [
                        items['sitename'],
                        
                    items['county'],
                    items['aqi'],
                    items['status'],
                    items['pm2.5'],
                    items['datacreationdate'],
                    
                    
                    
                    items['latitude'],
                    items['longitude'],
                    
                    ]
                outerlist.append(innerlist)

        
        
        
        return outerlist
     
def insert_data_into_db(data:list[list]):
    #connect to sqlite
    conn = sqlite3.connect('AQI_00.db')
    cursor = conn.cursor()

    insertSQL='''
    IGNOR OR INSERT INTO RECORDS(sitename,county,aqi,status,pm25,date,lat,lon)
    VALUES(?,?,?,?,?,?,?,?)

    '''
    for record in data:
        cursor.execute(insertSQL,record)

    conn.commit()
    cursor.close()
    conn.close()

def main():
    sitenames = get_sitenames()

    for sitename in sitenames:
        selected_data= get_selected_data(sitename)
        insert_data_into_db(selected_data)

if __name__ =='__main__':
    main()

