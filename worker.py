import requests
import psycopg2
import psycopg2.extras
from datetime import datetime
import logging

def fetch_data():
    api_token = 'cdf5a07c9452d64a'

    url = 'http://api.wunderground.com/api/' + api_token + '/conditions/q/CA/San_Francisco.json'
    r = requests.get(url).json()
    data = r['current_observation']

    location = data['observation_location']['full']  # city, state and observation location
    weather = data['weather']  # cloud, clear, etc
    wind_str = data['wind_string']  # pretty print version of wind speed and dir
    temp = data['temp_f']  # temperature in fahrenheit
    humidity = data['relative_humidity']  # humidity with %
    precip = data['precip_today_string']  # displays total precip in inches and mm
    icon_url = data['icon_url']  # url for weather icon (clear, cloud, rainy, etc)
    observation_time = data['observation_time']  # pretty print of observation time

    #open db
    try:
        conn = psycopg2.connect(dbname='d3enlk294pbi15', user='tleawaslframmo', host='ec2-107-22-236-252.compute-1.amazonaws.com', password='6f347648c1a4b2a5aeb99ef699a0aba2d4f4a64d614b68c6159e180dc2b60e3e')
        print('Opened DB successfully')
    except:
        print(datetime.now(), "Unable to connect to the database")
        logging.exception("Unable to open the database")
        return
    else:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # write data to database
    cur.execute("""INSERT INTO finalassignmentapp_reading(location, weather, wind_str, temp, humidity, precip, icon_url, observation_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", (location, weather, wind_str, temp, humidity, precip,
                                                            icon_url, observation_time))

    conn.commit()
    cur.close()
    conn.close()

    print("Data Written", datetime.now())

fetch_data()