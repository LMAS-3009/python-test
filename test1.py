import requests as req
from selenium import webdriver
import time
import os
import json

url = "https://api.telegram.org/bot1213410968:AAG6TJMmCfBjIVachFE_kKmI98kchXXFSLk/"
def getbotname():
    res = req.get(url+"getMe")
    res = res.json()
    name = res["result"]["username"]
    return name

def getmessages_id(): #get Latest Messages_id
    res = req.get(url + "getUpdates")
    res = res.json()
    res = res["result"]
    message_id = res[len(res)-1]["message"]["chat"]["id"]
    return message_id

def getmessages(): #get Latest Messages
    res1 = req.get(url + "getUpdates")
    res1 = res1.json()
    res1 = res1["result"]
    message = res1[len(res1)-1]["message"]["text"]
    return message

def message_count(): # get total Message count
    res2 = req.get(url + "getUpdates")
    res2 = res2.json()
    res2 = res2["result"]
    return len(res2)



def sendmessage(message):
    id = getmessages_id()
    print(id) 
    try:
        pos = {"chat_id":id,"text":message}
        res = req.post(url + "sendmessage",data=pos)
        print(res)
    except Exception as e:
        print(e)
        

def convert(lst,lst1,lst3):
    try:
        x = lst.index(max(lst))
        sendmessage("Maximum Price is "+max(lst)+"\n Name is "+lst1[x]+"\n"+" Link is "+lst3[x])
    except:
        print("exception")
    
    
def new(lst,lst1,lst3):
    print(len(lst))
    #li.append(res)
    #print(li)
    print(lst)
    time.sleep(5)
    if(lst!=None):
        convert(lst,lst1,lst3)
    else:
        sendmessage("Unable to find the product")


def amazon(name):
    li =[]
    path ="C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.amazon.in/")
    
    
    search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
    search.send_keys(name)
    search.click()
    
    search_btn = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
    search_btn.click()
    
   
    products = []
    products1 = []
    products2 = []
    
    page = 1
    
    while True:
        for i in driver.find_elements_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]'):
            counter = 0
            for element in i.find_elements_by_xpath('//div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a'):
                should_add = True
                name = ""
                price = ""
                link = ""
                try:
                    name = i.find_elements_by_tag_name('h2')[counter].text
                    #print(name)
                    if(name.find(name) == -1 ):#or name.find("Echo") == -1):
                        #print("no")
                        continue
                    else:
                        price = element.find_element_by_class_name('a-price').text
                        #print(price)
                        link = element.find_elements_by_xpath('//h2/a')[counter].get_attribute("href")
                        #print(link)
                        #link = i.find_elements_by_xpath('//h2/a')[counter].get_attribute("href")
                        #products1.append("Name")
                        products.append(price)
                        products1.append(name)
                        products2.append(link)
                        
                except Exception as e:
                    print(e)
                    should_add = False
                counter = counter + 1
                #print(products)
                #print(convert(products))
        new(products,products1,products2)
        page = page - 1
        if page == 0:
            break
        print(page)
    time.sleep(10)
    driver.close()

        
        #print(i.find_elements_by_tag_name('span')[counter].text)
        #print(i.find_element_by_class_name('a-price').text)
        #print(i.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/a/span[1]/span[1]'))
#amazon()


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
            sendmessage(str(loc_name)+","+str(loc_country)+"\n"+"Timezone: "+str(loc_time_zone)+"\n"+"Is_day: "+str(is_day)+"  Weather_discription: "+str(weather_dis)+"\n"+"Today Temperature: "+str(curr_temp)+"*C  "+i+"\n"+"Wind Speed:  "+str(wind_speed)+"kmph"+"  Humidity:  "+str(humidity)+"  CloudCover:  "+str(cloud_cover)+"%"+ " Wind Direction:  "+str(direction))
    except:
        sendmessage(str(res["error"]["type"])+"\n"+str(res["error"]["info"])+"\n"+"Try again next month")

def main():
    count_new = message_count()
    while(True):
        if(message_count()==count_new):
                message = getmessages()
                if(message == "hi" or message == "Hi"):
                    sendmessage("Welcome to new world")
                elif(message == "what is your name" or message == "What is your name"):
                    sendmessage(getbotname())
                elif("search" in message or "Search" in message):
                    if("amazon" in message):
                        first = message.find("{")
                        second = message.find("}")
                        name = message[first+1:second]
                        print(name)
                        amazon(name)

                    elif("snapdeal" in message):
                        for i in message.split():
                            if i.startswith("/"):
                                sendmessage("We are still working on it...")

                    elif("flipkart" in message):
                        for i in message.split():
                            if i.startswith("/"):
                                sendmessage("We are still working on it...")
                                
                elif(message == "Today's weather" or message == "today's weather" or message == "Today weather"):
                    weather_location()

                elif("github" in message):
                    if(getmessages_id()<0):
                        sendmessage("It is not applicable in groups")
                    elif(getmessages_id()>0):
                        sendmessage("we are still working on it")
                elif(message=="help" or message == "Help"):
                    sendmessage("Hello,\n I can help your make a github repo and also i can find maximum deails in amazon\n cmd: Today's weather - For getting a weather info\n cmd: search for {apple watch} in amazon - For getting a minimum cost watch for example search for{apple phone} in amazon")

                else:
                    sendmessage("I am unable to understand?")

                count_new+=1
                time.sleep(0.2)
        print(count_new)


main()
