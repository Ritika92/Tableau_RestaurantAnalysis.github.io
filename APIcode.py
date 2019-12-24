
# coding: utf-8

# In[ ]:


import requests
import ast
import json
import csv
base_url = "https://developers.zomato.com/api/v2.1/"

#zomato API returns only 20 records per call. There are 40 cities in total and 80 restaurant details per city
#entity id means city id from 1-40
x = [0,21,41,61]
for z in range(1,40):
    for i in x:
        entity_id = z
        entity_typ="city"
        start = i
        count ="20"
        limit =""
        
        #connecting with the API
        if str(limit).isalpha() == True:
            raise ValueError('LimitNotInteger')
        headers = {'Accept': 'application/json', 'user-key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
        r = (requests.get(base_url + "search?entity_id=" + str(entity_id) + "&entity_type=" + entity_typ + "&start=" + str(start) + "&count=" + count, headers=headers).content).decode("utf-8")
        a = json.loads(r)

        #collecting data returned by API in a dictionary
        restaurant_details_city = {}
        for res in a["restaurants"]:
            restaurant_details_city.update(({res['restaurant']['id'] : [res['restaurant']['name'],res['restaurant']['location']['city'],res['restaurant']['location']['city_id'],res['restaurant']['location']['latitude'],res['restaurant']['location']['longitude'],res['restaurant']['average_cost_for_two'],res['restaurant']['price_range'],res['restaurant']['user_rating']['aggregate_rating'],res['restaurant']['user_rating']['rating_text'],res['restaurant']['user_rating']['votes'],res['restaurant']['has_online_delivery'],res['restaurant']['is_table_reservation_supported'],[res['restaurant']['cuisines']]]}))


        #writing all the data collected in csv
        with open('restaurant_city_final.csv', 'a') as f:
            for key in restaurant_details_city.keys():
                f.write("%s,%s\n"%(key,restaurant_details_city[key])) 

