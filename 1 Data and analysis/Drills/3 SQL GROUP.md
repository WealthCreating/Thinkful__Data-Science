### What was the hottest day in our data set? Where was that?
> SELECT
	Date, MaxTemperatureF, ZIP
FROM
	weather
GROUP BY Date
ORDER BY MaxTemperatureF desc
LIMIT 1

---
### How many trips started at each station?
>SELECT start_station, COUNT(*) as trips_started
FROM trips
GROUP BY start_station


---
### What's the shortest trip that happened?
> SELECT duration
FROM trips
ORDER BY duration asc
LIMIT 1


---
### What is the average trip duration, by end station?
> SELECT 
	end_station,
	SUM(duration) / COUNT(*) as average_trip_duration
FROM
	trips
GROUP BY
	end_station
