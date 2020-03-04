#!/usr/bin/env python3

import datetime
from datetime import timedelta
import forecastio
import enum

API_KEY = "e07c570e1f5f85a42dacce70bc6c63ce"
CITYNAME = 0
LATITUDE = 1
LONGITUDE = 2
TEMP_SCALE = 3
GMT_OFFSET = 4
TZ_ABBREV = 5

#Define City Characteristics
citydata = [[ "Newport Beach, CA. USA", 33.6189, -117.9298, "Farenheit", -8, "PST" ],
            [ "Melbourne, AUS", -37.8136, 144.9631, "Celsius", +11, "AEDT" ]]

for i in range(len(citydata)):
    city = citydata[i][CITYNAME]
    lat = citydata[i][LATITUDE]
    long = citydata[i][LONGITUDE]
    scale = citydata[i][TEMP_SCALE]
    tz = citydata[i][TZ_ABBREV]

    #Get Temperature info
    forecast = forecastio.load_forecast(API_KEY, lat, long)
    current = forecast.currently()
    
    tz_time = current.time + timedelta(hours=citydata[i][GMT_OFFSET])
   
    print ("Current Temp in", city, "is ",current.temperature,"degrees", scale, "at ",tz_time,citydata[i][TZ_ABBREV] )
    print ()
