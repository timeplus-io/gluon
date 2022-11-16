case = {
  "s-tail": [
    "streaming tail",
    '''SELECT _tp_time,time,cid,gas_percent
FROM car_live_data
WHERE gas_percent < 60''',
  ],
  "s-downsampling": [
    "downsampling",
    '''SELECT window_start,cid,
    avg(gas_percent) AS avg_gas_percent,
    avg(speed_kmh) AS avg_speed
FROM tumble(car_live_data, 10s)
GROUP BY window_start,cid
  ''',
  ],
  "s-agg-recent": [
    "past hour sum",
    '''SELECT sum(amount)
FROM trips
EMIT LAST 1h''',
  ],
  "s-time-travel": [
    "time travel",
    '''SELECT window_start, count(*)
FROM tumble(bookings, 10s)
WHERE action = 'add'
GROUP BY window_start
EMIT LAST 2h''',
  ],
  "s-mview": [
    "materialized view",
    "-- creat e materialized view today_revenue as select sum(amount) from trips where end_time > today()\nSELECT '''sum(amount)''' FROM today_revenue",
  ],
  "s-drop-late": [
    "drop late event",
    '''SELECT window_start, window_end, sum(amount), count(*)
FROM tumble(trips, end_time, 10s)
GROUP BY window_start, window_end''',
  ],
  "s-wait-late": [
    "wait late event",
    '''SELECT window_start, window_end,sum(amount),count(*)
FROM tumble(trips, end_time, 10s)
GROUP BY window_start, window_end
EMIT AFTER WATERMARK AND DELAY 5s''',
  ],
  "s-top-k": [
    "top k",
    '''SELECT window_start, top_k(cid, 3) AS popular_cars
FROM tumble(bookings, 1h)
GROUP BY window_start  
EMIT LAST 2h''',
  ],
  "s-max-k": [
    "max k",
    '''SELECT window_start, max_k(amount, 3) AS longest_trips
FROM tumble(trips, 1h)
GROUP BY window_start
EMIT LAST 2h''',
  ],
  "s-min-k": [
    "min k",
    '''SELECT window_start, min_k(amount, 3) AS shortest_trips
FROM tumble(trips, 1h)
GROUP BY window_start
EMIT LAST 2h''',
  ],
  "s-over-time": [
    "over time compare",
    '''SELECT window_start,count(*) AS num_of_trips,
    lag(num_of_trips) AS last_min_trips,
    num_of_trips - last_min_trips AS gap
FROM tumble(trips, 10s)
GROUP BY window_start''',
  ],
  "car-in-use": [
    "cars in use",
    '''SELECT window_start, count(distinct cid)
FROM tumble(car_live_data, 10s)
WHERE in_use
GROUP BY window_start''',
  ],
  "top-10": [
    "cars with top revenue",
    '''SELECT cid, sum(amount) AS revenue
FROM trips
INNER JOIN bookings ON trips.bid = bookings.bid
WHERE end_time > today()
GROUP BY cid
ORDER BY revenue DESC LIMIT 10
SETTINGS query_mode = 'table' ''',
  ],
  "t-mask": [
    "mask",
    '''SELECT uid,
    replace_regex(credit_card, '(\\d{4})(\\d*)(\\d{4})', '\\1***\\3') AS card
FROM user_info''',
  ],
  "t-derive": [
    "derive",
    '''SELECT uid,
    concat(first_name, ' ', last_name) AS full_name,
    year(today()) - year(to_date(birthday)) AS age
FROM user_info''',
  ],
  "t-lookup": [
    "lookup",
    '''SELECT time,cid,c.license_plate_no AS license,gas_percent, speed_kmh
FROM car_live_data
INNER JOIN car_info AS c ON car_live_data.cid = c.cid''',
  ],
}