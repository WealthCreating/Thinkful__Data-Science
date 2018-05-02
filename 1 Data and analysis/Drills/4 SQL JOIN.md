### What are the three longest trips on rainy days?
> select
	trips.duration
from
	trips
join
	weather
on
	trips.zip_code = weather.ZIP
where
	weather.Events = 'Rain'
order by
	trips.duration desc
limit 3


---
### Which station is full most often?
> select 
    stations.station_id,
    COUNT(*)
from 
    stations
join 
    status
on 
    stations.station_id = status.station_id
where 
    status.docks_available = 0
group by 
    stations.station_id
order by 
    status.docks_available desc
limit 1

---

### Return a list of stations with a count of number of trips starting at that
### station but ordered by dock count.
> select
	stations.dockcount, stations.name, COUNT(trips.trip_id)
from
	stations
join
	trips
on
	stations.name = trips.start_station
group by
	stations.name
order by
    stations.dockcount
	

---
### (Challenge) What's the length of the longest trip for each day it rains
### anywhere?


> with
	trip_data
	
AS (
select
	start_date Date,
	MAX(duration) duration
from
	trips
group by 1
)

select
	t.Date,
	t.duration
from
	trip_data t

join
	weather w
on
	t.Date = w.Date
join
	trips
on
	t.Date = trips.start_date
where
    weather.Events = 'Rain'
group by 1
