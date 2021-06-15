# sqlalchemy-challenge
## Step 1 - Climate Analysis and Exploration
Use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
Resources:  [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) 

Steps:
* Use SQLAlchemy `create_engine` to connect to your sqlite database.
* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.
* Link Python to the database by creating a SQLAlchemy session.

### Precipitation Analysis
* ID the most recent date in the data set.
* Using this date, retrieve the average precipitation per day for the previous 12 months. The query should be sorted by date ascending. **Note** you do not pass in the date as a variable to your query.
* Load the query results into a Pandas DataFrame and set the index to the date column.
* Plot the results using the DataFrame `plot` method. 
* Use Pandas to print the summary statistics for the precipitation data. 
* Close out your session.
*
### Station Analysis
* Design a query to calculate the total number of stations in the dataset.
* Design a query that lists all stations with their corresponding observation count in descending order (observation count corresponds to the number of rows per station).
* Which station id is the most active (i.e., has the greatest number of observations)?
* Calculate the lowest, highest, and average temperature for that station id (i.e., the one with the greatest number of observations).
* Design a query to retrieve the last 12 months of temperature observation data (TOBS) for the most active station.
* Plot the results as a histogram with `bins=12`.
* Close out your session.

- - -

## Step 2 - Climate App
Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.
* Use Flask to create your routes.

### Routes
* `/`
  * Home page.
  * List all routes that are available.
* `/api/v1.0/precipitation`
  * Using the query from part 1 (most recent 12 months of precipitation data), convert the query reszults to a dictionary using `date` as the key and `prcp` as the value.
  * Return the JSON representation of your dictionary (note the specific format of your dictionary as required from above).
* `/api/v1.0/stations`
  * Return a JSON list of stations from the dataset.
* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the **most active station** for the most recent 12 months of data.
  * Return a JSON list of temperature observations (TOBS) for that year.
* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
  * Create a query that returns the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  * When given the start date only, calculate min, max, and avg for all dates greater than and equal to the start date.
  * When given the start and the end date, calculate the minimum, average, and maximum obvserved temperature for dates between the start and end date inclusive.
  * Return a JSONified dictionary of these minimum, maximum, and average temperatures.


### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?
* You may either use SQLAlchemy or pandas's `read_csv()` using `hawaii_measurements.csv` to perform this portion.
* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.
* Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

.
Discussion: The independent-samples t-test (or independent t-test, for short) compares the means between two unrelated groups on the same continuous, dependent variable. An indepedent t-test is appropriate because the June and Decemeber are two different datasets. The null hypothesis is that the means for June and December is equal. 

The t-value is 4.62 and the p-value is 0.0003. Because the p-value is less than 0.05, we reject the null hypothesis and we conclude that the difference of means in temperature between June and December is different from zero. 

### Temperature Analysis II

* You are looking to take a trip from August first to August seventh of this year, but are worried that the weather will be less than ideal. Using historical data in the dataset find out what the temperature has previously looked like.
* Create a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.
* Use the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from a previous year (i.e., use "2017-08-01").
* Plot the min, avg, and max temperature from your previous query as a bar chart.
  * Use "Trip Avg Temp" as the title.
  * Use the average temperature as the bar height (y value).
  * Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).
  

### Daily Rainfall Average

* Now that you have an idea of the temperature lets check to see what the rainfall has been, you don't want a when it rains the whole time!
* Calculate the rainfall per weather station using the previous year's matching dates.
* Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.

### Daily Temperature Normals

* Calculate the daily normals across all weather stations for all previous years with matching month and day for your trip (August first to August seventh, inclusive). Normals are the averages for the min, avg, and max temperatures.
* Create a function called `daily_normals` that will return the daily normals for a specific month and day in **tuple format**. This date string will be in the format `%m-%d`. Be sure to use all historic TOBS that match that date string.
* Use the `daily_normals` function to calculate the normals for each date string and append the resulting tuples to a list (so you will end up with a list of tuples).
* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
* Use Pandas to plot an area plot (`stacked=False`) for the daily normals.
