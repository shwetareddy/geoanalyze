#Overview

Project is host at [http://shwetareddy.pythonanywhere.com/](http://shwetareddy.pythonanywhere.com/)

##Technology:
- Django(python)  
- MySql
- Google Maps
- Bootstrap

##Data migration:
- For each row I took the latitude and longitude of the next row as the drop off points and then skipped that row. Due to the limit on daily CPU allowance, I could only import the data for April and some from May. I created a django [management command](https://github.com/shwetareddy/geoanalyze/blob/master/geoanalyzer/management/commands/load_trips.py) to import data.

##Design:
- First page load the map that can be drawn on and displays a bar chart with the total number of trips by month. The number of trips is so large that I decided not to show any markers on first load on the map.
- The selection of a polygon on the map triggers a Javascript function that retrives all the pickup and dropoff points in the selected area. Ideally in a production setting a Spatial database should be used like PostGIS, SpatiaLite or even Postgres with geometry fields so only points contained with a given polygon can be queried. In lieu of that I pass the max and min latitude and longitude as north, south, east and west respectively to the api endpoint and the all points within that are returned. I determined if all those points are within the polygon in Javascript.
- Once the data is returned their are filters to show only the markers in certain time of the day or the most common pickups and drop offs.

##Analysis
- Midtown is by far the most popular area for pickups and drop offs. Its busiest in the evening followed by afternoon, night and morning. Metro stations are the most popular location for pickup or drop off.
- Similarly Downtown Manhattan is also busy near metro station and couple of blocks around it. Its the busiest in evening and night. Westside is more busy than the Eastside.
- Unlike Midtown and Downtown, Upper East side and Upper West side are more busy in the morning.

#Improvements
- Spatial Databse or fields
- Cache queries
- Map APIs/Interface without quoata limit
- Better design