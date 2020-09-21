The Climate Measurement Project

![routes](https://github.com/EmmaLimoli/sqlalchemy-challenge/blob/master/completed_images/Screen%20Shot%202020-08-18%20at%206.54.55%20PM.png)

The Goal:
The goal for this project was to use SQLalchemy to study the climate in Hawaii and then use Flask to make the data live on a website. In this project, I analyzed the measurements of precipitation for specific stations in Hawaii. Once the data was pulled, I wanted to showcase it by using Flask to create different webpages that showed specific information.

How This Was Accomplished (Part One):
The first step in this project was to import the dependencies in Jupyter Notebook. I used dependencies such as Matplotlib, Numpy, Pandas, and SQLalchemy. Once the dependencies were implemented, I created an engine to the Hawaii SQLite database. I added reflect to the existing database into the new model to reflect the tables that are in the database. Then to make sure that I had the proper data, I viewed the classes using Automap. The two classes I used were measurement and station. I also created a session between Python to the database to ensure a secure connection.

Once everything was connected, I used inspector to run the columns. This helped to see the types of columns in both of the sets of data. This also helped when I needed to filter out specific data to better understand which columns names were in which dataset. 

After inspecting the measurements and stations, I used engine execute to fetchall for measurement and then viewed the function count using Session. I needed to see the earliest and the latest date for the measurement dataset to better filter out the information I needed. I decided to look at the previous year of data in the set so I filtered out everything from 08/22/2016 to 08/24/2017 and the measurement of precipitation. Doing an order by, it was easier to sort through the dates. 

I converted the query results into a Pandas dataframe and set the index to date, so I could turn it into a bar graph to better see the data. The x-axis was by date while the y-axis was by inches of precipitation. To also better understand the date, I used describe to see the count of precipitation, mean, STD, min, max, etc. This helped to paint a better picture of the precipitation measurements for the year between August 2016 and August 2017.

Next, I focused on station. Similarly to measurement, I counted the total amount of stations to ensure no data was missed. Then I filtered the stations by the most active. I decided which stations were the most active based on the rows of data and how many times a station was mentioned. I listed the stations and the number of times they were listed.

![active stations](https://github.com/EmmaLimoli/sqlalchemy-challenge/blob/master/completed_images/Screen%20Shot%202020-08-18%20at%206.55.30%20PM.png)

For each of the stations, I calculated the maximum, average, and minimum. I then filtered out by the highest number of observations. I pulled out the station with the highest number of observations and filtered out the max, avg, and min. I took the station with the highest number of observations and looked at the last year of temperature observations. By filtering out the date and the station, I ordered the measurements of that station by the date and printed it out. Once the date was gathered, I put it into a dataframe and converted it into a histogram. 

To create the histogram, I used bins and looked at the max/min date and tobs to figure out the correct groupings. In the histogram, I labeled the x-axis as temperature and the y-axis as frequency for the most active station in one year.

Once the histogram was created, I moved on to app.py. 

![bar graph for PRCP](https://github.com/EmmaLimoli/sqlalchemy-challenge/blob/master/completed_images/prcp_date.png)
![histogram](https://github.com/EmmaLimoli/sqlalchemy-challenge/blob/master/completed_images/histogram.png)

Part Two:
In Flask, I used jsonify to convert the API data into a json response object. I used the same dependencies in the Jupyter Notebook as well as the same set up. Once the Flask was set up, I created the routes. There were six routes in this project. There's the homepage, the precipitation, list of stations, temperature observations or TOBS, the start date, and then start and end date route. 

In the homepage, you'll find the routes for each page that was built out. In the precipitation page, there's the query results that use a dict to loop through the date and precipitation. The next page is the list of stations, which prints out the stations in Hawaii. TOBS is similar to the precipitation page. I used a loop and a dict to print out the date and the TOBS. The pages that have a date such as the precipitation and TOBs analyzed the last year (08/2016-08/2017).

The start date page provides the minimum, maximum, and the average of the dates given. I used a dict and a loop to pull in the aforementioned information with the date. The start and end date pages only analyze two weeks that were given in the code. The only difference between these two pages is that there's an end date given and the last page analyzes a small sect of the date.

![breakdown of routes](https://github.com/EmmaLimoli/sqlalchemy-challenge/blob/master/completed_images/Screen%20Shot%202020-08-19%20at%203.21.48%20PM.png)

Conclusion:
In conclusion, I was able to determine the station that's the most active in Hawaii, analyze the rain fall, and create a site to store the data. I also created visualizations to better understand and showcase the data. While the dates are on the older side, I can continue analyzing the data and determine if there are changes in the weather pattern in Hawaii for the future.

Tools Used: Pandas, Numpy, Flask, datetime, matplotlib, SQLalchemy, SQLalchemy ORM, reflect, automap base



