"""
Arrow is a Python library that offers a sensible and human-friendly \
approach to creating, manipulating, formatting and converting dates, \
times and timestamps. It implements and updates the datetime type, \
plugging gaps in functionality and providing an intelligent module API \
that supports many common creation scenarios. Simply put, it helps \
you work with dates and times with fewer imports and a lot less code.
"""

import arrow

# getting the UTC time
now = arrow.utcnow()
print("UTC in Arrow")
print(now)
print("Type:", type(now))
print("Time Zone:", now.tzinfo)
# similar function in datetime - Depreciated
# import datetime
# datetime.datetime.utcnow()

# converting arrow to datetime
now = arrow.utcnow()
now = now.datetime
print("\nConverting Arrow to Datetime")
print(now)
print("Type:", type(now))

# removing the Timezone
# using naive will convert it from Type Arrow to Datetime
now = arrow.utcnow()
now = now.naive
print("\nTime without TimeZone")
print(now)

# get the current time, i.e. the system time from which the program is running
# arrow bydefault includes the Timezone
now = arrow.now()
print(now)
# output is tzlocal(), implies local timezone
print(now.tzinfo)

# creating a timestamp
dt = arrow.Arrow(
    2023, 6, 19, 13, 15, 0
)  # i have not added timezone, so it takes utc as default tz
print("\nCreating Timestamp")
print(dt)

# ---------------------- Dealing with TimeZones ------------------------------
# getting the time of a specific tz
dt = arrow.now("Asia/Tokyo")
print("\nGetting time at Asia/Tokyo TZ")
print(dt)

dt_changed = dt.to("US/Central")
print("\nCoverting the Above Timezone to US/Pacific")
print(dt_changed)

# converting an incoming data to naive timezone
# using naive will convert it from Type Arrow to Datetime
date_str = "2023-09-18T10:30:00+07:00"
dt = arrow.get(date_str).to("UTC").naive
print(f"\nChaning {date_str} to naive UTC without TZ")
print(dt)
