## Let's confirm some of this new knowledge with a few basic exercises. Write SQL queries to return:

---

#### The ID's and durations for all trips of duration greater than 500, ordered by duration.
> SELECT
> 	trip_id, duration
> FROM
> 	trips
> WHERE
> 	duration > 500
> ORDER BY duration desc

#### Every column of the stations table for station id 84.
> SELECT
> 	*
> FROM
> 	stations
> WHERE
> 	station_id = 84

#### The min temperatures of all the occurrences of rain in zip 94301.
> SELECT
>	MinTemperatureF
> FROM
> 	weather
> WHERE
> 	ZIP = 94301 AND Events = 'Rain'
