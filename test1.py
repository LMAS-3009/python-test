import requests as req
import json

def weather_location():
    weather_url = "http://api.weatherstack.com/current?access_key=9d08ecd871eadd427c4f59e3389198ed&query=Hyderabad,Telangana,India"
    res = req.get(weather_url)
    res = res.json()
    try:
        location = res["location"]
        loc_name = location["name"]
        loc_country = location["country"]
        loc_time = location["localtime"]
        loc_time_zone = location["timezone_id"]
        logo = res["current"]["weather_icons"]
        current = res["current"]
        curr_temp = current["temperature"]
        humidity = current["humidity"]
        wind_speed = current["wind_speed"]
        is_day = current["is_day"]
        wind_direction = current["wind_dir"]
        cloud_cover = current["cloudcover"]
        weather_dis = current["weather_descriptions"]
        for i in logo:
            if (str(wind_direction) == "W"):
                direction = "West"
            elif (str(wind_direction) == "N"):
                direction = "North"
            elif (str(wind_direction) == "E"):
                direction = "East"
            else:
                direction = "South"
            print(str(loc_name)+","+str(loc_country)+"\n"+"Timezone: "+str(loc_time_zone)+"\n"+"Is_day: "+str(is_day)+"  Weather_discription: "+str(weather_dis)+"\n"+"Today Temperature: "+str(curr_temp)+"*C  "+i+"\n"+"Wind Speed:  "+str(wind_speed)+"kmph"+"  Humidity:  "+str(humidity)+"  CloudCover:  "+str(cloud_cover)+"%"+ " Wind Direction:  "+str(direction))
    except:
        print(str(res["error"]["type"])+"\n"+str(res["error"]["info"])+"\n"+"Try again next month")

weather_location()
