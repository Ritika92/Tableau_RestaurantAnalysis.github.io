## Problem Statement:
Help a new Restaurateur decide in which city and for which cuisine he/she should open up a new restaurant. And what important service should be provided for a successful venture.
## Pipeline
![Screenshot](https://user-images.githubusercontent.com/59153134/71398388-1f343b80-25d5-11ea-9deb-2fcab2c953d8.jpg)
## Link to Tableau Story
https://ritika92.github.io/Tableau_RestaurantAnalysis.github.io/
## Data Source:
Zomato API https://developers.zomato.com/documentation
## Data collected using:
Python script (available in this repository). The csv file created by the python script is also available in this repository. 
## Challenges faced:
Zomato API only sends back 20 records per call. There were 40 cities and each city had data for 80 restaurants. Collecting data was difficult given the city ids had to be searched manually through the API.
There are many methods the API provides to fetch different types of data. Finding the useful one was time consuming and difficult.
## Tableau features used:
- Maximum types of charts used such as bar, stacked bar, shapes, maps etc.

- Actions used. On clicking a city on the map, the bar chart on the same dashboard shows what cuisines are available in the selected city.

- Calculated fields used to categorize cuisines.

- Data splitting to get meaningful data in each column.





