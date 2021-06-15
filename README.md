# sqlalchemy-challenge

Use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis completed using SQLAlchemy ORM queries, Pandas, and Matplotlib, Flask.
Steps:
* Use SQLAlchemy `create_engine` to connect to your sqlite database.
* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.
* Link Python to the database by creating a SQLAlchemy session
Resources:  [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) 

## Step 1 - Climate Analysis and Exploration

### Precipitation Analysis
Average precipitation per day for the previous 12 months. 

![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/31d54e1f35c016526c9c8dc38454eced112b6eb7/Images/precipitation_analysis_AI.PNG)


### Station Analysis
The lowerst, highest, and average temperature (TOBS) in the last 12 months for the most active station.
* 
![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/31d54e1f35c016526c9c8dc38454eced112b6eb7/Images/station_histogram_AI.PNG)

- - -

## Step 2 - Climate App
Design a Flask API based on the queries that you have just developed.

![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/24567c3ece4e710d977ad69ca2785905a26a6308/Images/home_route_AI.PNG)

### Temperature Analysis I
T-test of average temperature in June and December at all stations across all available years in the dataset. 
* 
![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/2e587c12365da07f1e2d5b91b294e1ca819f17d3/Images/t_test.PNG)<br>
.
Discussion: The independent-samples t-test (or independent t-test, for short) compares the means between two unrelated groups on the same continuous, dependent variable. An indepedent t-test is appropriate because the June and Decemeber are two different datasets. The null hypothesis is that the means for June and December is equal. 

The t-value is 4.62 and the p-value is 0.0003. Because the p-value is less than 0.05, we reject the null hypothesis and we conclude that the difference of means in temperature between June and December is different from zero. 

### Temperature Analysis II
For 8/1/2017 - 8/7/2017, bar chart of average temperature with peak-to-peak (TMAX-TMIN)  as error bar. 

![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/31d54e1f35c016526c9c8dc38454eced112b6eb7/Images/trip_temp.PNG)
  

### Daily Rainfall Average
For 8/1/2017 - 8/7/2017, rainfall at each station. 

![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/31d54e1f35c016526c9c8dc38454eced112b6eb7/Images/station_precip.PNG)

### Daily Temperature Normals

For August 1 - 7 for all previous year, area plot of daily normal temperature. 

![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/31d54e1f35c016526c9c8dc38454eced112b6eb7/Images/trip_normal_temp.PNG)
