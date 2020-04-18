tot = int(input("enter number of seconds: "))
day = int(((tot / 60) / 60) / 24)
hour = int(((tot / 60) / 60) % 24)
mins = int((tot / 60) % 60)
sec = tot % 60
d = str(day)
h = str(hour)
m = str(mins)
s = str(sec)
if day < 10:
    d = "0" + d
if hour < 10:
    h = "0" + h
if mins < 10:
    m = "0" + m
if sec < 10:
    s = "0" + s
print(d, ":", h, ":", m, ":", s)
