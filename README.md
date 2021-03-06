# sqlalchemy-challenge

Use Python and SQLAlchemy to do climate analysis and data exploration of your climate database. All of the following analysis completed using SQLAlchemy ORM queries, Pandas, and Matplotlib, Flask.
Steps:
* Use SQLAlchemy `create_engine` to connect to your sqlite database.
* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.
* Link Python to the database by creating a SQLAlchemy session
Resource: Hawaii weather station dataset [hawaii.sqlite](Resources/hawaii.sqlite) 

## Table of Contents ##
* [Precipitation Analysis](https://github.com/adriana-icasiano/sqlalchemy-challenge#Precipitation-Analysis)
* [Station Analysis](https://github.com/adriana-icasiano/sqlalchemy-challenge#Station-Analysis)
* [Climate App](https://github.com/adriana-icasiano/sqlalchemy-challenge#Climate-App)
* [Bonus](https://github.com/adriana-icasiano/sqlalchemy-challenge#Bonus)
* [Temperature Analysis I](https://github.com/adriana-icasiano/sqlalchemy-challenge#Temperature-Analysis-I)
* [Temperature Analysis II](https://github.com/adriana-icasiano/sqlalchemy-challenge#Temperature-Analysis-II)
* [Daily Rainfall Average](https://github.com/adriana-icasiano/sqlalchemy-challenge#Daily-Rainfall-Average)
* [Daily Temperature Normals](https://github.com/adriana-icasiano/sqlalchemy-challenge#Daily-Temperature-Normals)

## Climate Analysis and Exploration

### Precipitation Analysis
Average precipitation per day for the previous 12 months. 

![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/31d54e1f35c016526c9c8dc38454eced112b6eb7/Images/precipitation_analysis_AI.PNG)


### Station Analysis
The lowerst, highest, and average temperature (TOBS) in the last 12 months for the most active station.
* 
![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/31d54e1f35c016526c9c8dc38454eced112b6eb7/Images/station_histogram_AI.PNG)

- - -

## Climate App
Design a Flask API based on the queries that you have just developed.

![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/24567c3ece4e710d977ad69ca2785905a26a6308/Images/home_route_AI.PNG)

### Bonus
### Temperature Analysis I
T-test of average temperature in June and December at all stations across all available years in the dataset. 
* 
![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/2e587c12365da07f1e2d5b91b294e1ca819f17d3/Images/t_test.PNG)<br>
.
Discussion: The independent-samples t-test (or independent t-test, for short) compares the means between two unrelated groups on the same continuous, dependent variable. An indepedent t-test is appropriate because the June and Decemeber are two different datasets. The null hypothesis is that the means for June and December is equal. 

The t-value is 4.62 and the p-value is 0.0003. Because the p-value is less than 0.05, we reject the null hypothesis and we conclude that the difference of means in temperature between June and December is different from zero. 

### Temperature Analysis II
For 8/1/2017-8/7/2017, bar chart of average temperature with peak-to-peak (TMAX-TMIN)  as error bar. 

![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/31d54e1f35c016526c9c8dc38454eced112b6eb7/Images/trip_temp.PNG)
  

### Daily Rainfall Average
For 8/1/2017-8/7/2017, average rainfall at each station. 

![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/31d54e1f35c016526c9c8dc38454eced112b6eb7/Images/station_precip.PNG)

### Daily Temperature Normals

For 8/1-8/7 for all previous year, area plot of daily normal temperature. 

![](https://github.com/adriana-icasiano/sqlalchemy-challenge/blob/31d54e1f35c016526c9c8dc38454eced112b6eb7/Images/trip_normal_temp.PNG)
