########## Task #2 ##########

import requests
import json
import datetime as dt
import pytz
import time

# Fetch today's date
date_today = dt.datetime.now(pytz.timezone('Asia/Singapore'))
year = date_today.year
month = date_today.month
day = date_today.day

# Get yesterday's date
## Special cases:
### Leap years
### January 1 to December 31 (change year)

if day == 1:
    if month != 1:  # Months aside from January
        year_yesterday = year
        month_yesterday = month-1
        if month in [1,3,5,7,10,12]:
            day_yesterday = 30
        elif month==3:  # March 1
            if year % 4 > 0:  # Non-leap year
                day_yesterday = 28
            else:  # Leap year
                day_yesterday = 29
        else:
            day_yesterday = 31
    else:  # January
        year_yesterday = year-1
        month_yesterday = 12
        day_yesterday = 31
else:
    year_yesterday = year
    month_yesterday = month
    day_yesterday = day-1

# Convert yesterday's date to UNIX format required by the API
date_yesterday = dt.datetime(year_yesterday, month_yesterday, day_yesterday)
unix_yesterday = time.mktime(date_yesterday.timetuple())
print("unix yesterday: ", unix_yesterday)

# Parameters of the API
API_key = '98e027721603ca32cead5457312b406a'
yesterday = str(int(unix_yesterday))
lat = "12.8797"
lon = "121.7740"
url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&units=metric&dt={yesterday}&appid={API_key}"
            # Added the parameter `units` to convert measurements into metric

# Fetch weather data
response = requests.get(url)
data = json.loads(response.text)
print(data['hourly'])

# Saving file as json
save_file = open("weather.json", "w")
json.dump(data['hourly'], save_file, indent = 6)
    # Saving only the hourly reports
save_file.close()