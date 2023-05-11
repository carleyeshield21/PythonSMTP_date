import datetime

now = datetime.datetime.now()
print(now)
print(type(now))

year = now.year
print(year)
print(type(year))

print(now.timetuple())