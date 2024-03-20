"""
Arrow is a Python library that offers a sensible and human-friendly \
approach to creating, manipulating, formatting and converting dates, \
times and timestamps. It implements and updates the datetime type, \
plugging gaps in functionality and providing an intelligent module API \
that supports many common creation scenarios. Simply put, it helps \
you work with dates and times with fewer imports and a lot less code.
"""

import arrow
import datetime

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

# --------------------- Formatting Datetimes ----------------------------------
# Converting raw time to str
# Reference - https://arrow.readthedocs.io/en/latest/guide.html#supported-tokens
dt = arrow.now()
dt_format = dt.format("MMMM D, YYYY (h:mm A ZZZ)")
print("\nFormatting Dates to String")
print(dt_format)

# Arrow has different built-in formatting standards
arw = arrow.now()
print("\nDifferent Builtin Formats in Arrow")
print(arw)  # standard ISO format
print("Format Atom:", arw.format(arrow.FORMAT_ATOM))
print("Format Cookie:", arw.format(arrow.FORMAT_COOKIE))
print("Format RSS:", arw.format(arrow.FORMAT_RSS))
print("Format RFC822", arw.format(arrow.FORMAT_RFC822))

# -------------------- Date Arithmetic -------------------------------
# doing date arithmetic is simple with Arrow, in datetime lib, we cannot
# add months or years directly but in Arrow we can

# shifting / moving the date
dt = arrow.utcnow()
# accepts both positive and negative numbers
dt_shifted = dt.shift(months=-1, days=3, years=4, hours=10, minutes=15)
print("\nShifting/Adding Dates")
print("Before:", dt)
print("After:", dt_shifted)

# Arrow handles DST(Daylight Savings) just fine while shifting
dt = arrow.get(datetime.datetime(2023, 3, 15, 3), "US/Central")
print("\nDST for date", dt)
print(dt.dst())  # 3600 seconds aka 1 hour

dt1 = arrow.get(datetime.datetime(2023, 12, 15, 3), "US/Central")
print("\nDST for date", dt1)
print(dt1.dst())  # 0 seconds

print("\nObserve the DT below - Notice how the UTC offset has changed!")
print("\nDT Before:", dt)
print("DT Shifted 8 months:", dt.shift(months=8))

# -------------------- Floor, Ceiling ------------------------
dt = arrow.utcnow()
print("\nDay:", dt)

# get the daystart
print("Day Start:", dt.floor("day"))

# hour end
print("Hour End:", dt.ceil("hour"))

# year start
print("Year Start:", dt.floor("year"))

# ----------------- Spans and Ranges ------------------------------
# Span - Gives the Beginning and Ending time for a given time

dt = arrow.utcnow()
print("\nDay:", dt)

# Getting the Begining and End Date for the Month for the Given Date
print("Beginning and End Date of Month:", *dt.span("month"))

# Getting the Begining and Ending Minute for the hour for the Given Date
# if time is 2024-06-18T16:23 then span is 2024-06-18T16:00 and 2024-06-18T16:59
print("Beginning and End Minute of the Hour for Given Date:\n", *dt.span("hour"))

# Getting the Begining and Ending Hour for the Day for the Given Date (i.e. is 00:00 and 23:59)
print("Beginning and End Hour of the Day for the Given Date:\n", *dt.span("day"))

# Ranges
start_dt = arrow.get(datetime.datetime(2023, 1, 10, 3, 30), "US/Central")
end_dt = arrow.get(datetime.datetime(2023, 1, 15, 0, 0), "US/Central")
print(f"\nPrinting Dates from {start_dt} till {end_dt}")
for dt in arrow.Arrow.range("day", start_dt, end_dt):
    print(dt)
# it hasn't included the last day because first day starts at 3AM but end date ends at 00AM

print("\nSpan Range - Get the Start Time and End Time for Ranges")
for dt in arrow.Arrow.span_range("day", start_dt, end_dt):
    print(dt[0], "-", dt[1])

# --------------------- Humanization and Localization -------------------------
dt_now = arrow.Arrow.utcnow()
dt_past = dt_now.shift(hours=-2)
dt_future = dt_now.shift(hours=2)

dt_past, dt_now, dt_future

# printing the dates for a human to understand
print("\nPrinting Dates with Humanize")
print(dt_past.humanize(dt_now))  # past is 2 hours behind present
print(dt_future.humanize(dt_past))  # future is 4 hours ahead past

# Adding more Granularity
print("\nAdding More Granularity and Languages")
print(dt_past.humanize(dt_now, granularity="minute"))  # past is 2 hours behind present
print(
    dt_future.humanize(dt_past, granularity=["hour", "minute"])
)  # future is 4 hours ahead past
print(
    dt_future.humanize(dt_past, granularity=["hour", "minute"], locale="hi")
)  # future is 4 hours ahead past
