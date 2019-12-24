## Problem Statement:
Help a new Restaurateur decide in which city and for which cuisine he/she should open up a new restaurant. And what important service should be provided for a successful venture.
## Data Source:
Zomato API https://developers.zomato.com/documentation
## Data collected using:
Python script (available in this repository)
## Challenges faced:
Zomato API only sends back 20 records per call. There were 40 cities and each city had data for 80 restaurants. Collecting data was difficult given the city ids had to be searched manually through the API.
There are many methods the API provides to fetch different types of data. Finding the useful one was time consuming and difficult.
## Tableau features used:
- Maximum types of charts used such as bar, stacked bar, shapes, maps etc.

- Actions used. On clicking a city on the map, the bar chart on the same dashboard shows what cuisines are available in the selected city.

- Calculated fields used to categorize cuisines.

- Data splitting to get meaningful data in each column.
## Solution suggested:
North Indian is the most common cuisine across the country which is decently priced. Noida is a metropolitan city close to National capital with very few restaurants serving North Indian cuisine and Noida has much lesser number of votes (meaning fewer people eating out) which means there is a solid potential market for “North Indian” cuisine in “Noida”. Also, Online delivery is an important service to provide as per the good ratings for restaurants providing online delivery.
Thus, the Restaurateur should open a “North Indian” cuisine restaurant in “Noida” and provide “Online delivery” service. 

## Pipeline
![Screenshot](Pipeline.png)

