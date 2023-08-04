
## Task #3

**From the data that you got from task#2, imagine reading millions or billions of rows from it. Describe a way on how you will design the table so that processing or querying the table will be optimized.**

There will be two main tables.

The first one will house all numeric weather variables, namely:
* `temp` = temperature
* `feels_like` = human perception of weather
* `pressure` = pressure
* `humidity` = humidity
* `dew_point` = atmospheric temperature
* `uvi` = UV index
* `clouds` = cloudyness in percent
* `visibility` = average visibility, maximum is 10m
* `wind_speed` = speed of wind
* `wind_deg` = direction of wind in degrees 
* `wind_gust` = wind gust
* `weather_id` = weather description id; a foreign key (referenced with the other table)

Furthermore, the first table will have the following identifying variables:
* dt = unix timestamp of the day
This `dt` variable can also be transformed into a human readable date and time format.

The second one will house descriptive text regarding the weather, with the following variables:
* `weather_id` = weather description id; both a primary key and a foreign key
* `main_desc` = general description about the weather (e.g., "Clouds")
* `description` = further description about the weather (e.g. "broken clouds")


---

## Task #4

**Assuming you want to deploy an automated solution for task#2 in a cloud setup to be available to an end user via a BI platform. Give a short high level description of a possible approach and some considerations that would affect your choices.**

I have yet to gain experience on data warehousing, data pipelines, cloud storage, and BI platforms. As of now they are simply abstract concepts to me, but from what I can gather from my own research, setting up a data pipeline to automate Task #2 may depend on several considerations. Generally, the two things below are surely on the top considerations.

* Cost: Storing data on cloud is costly. The choice for the cloud must also take into account running or storage costs.
* Efficiency: Related to cost, some cloud storages allow for fast download, but at a cost. The download speed and cost must be balanced to achieve optimum balance within budget.