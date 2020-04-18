days = int(input("enter number of days: "))
hours = int(input("enter number of hours: "))
mins = int(input("enter number of minutes: "))
sec = int(input("enter number of seconds: "))
ds = days * 24 * 60 * 60
hs = hours * 60 * 60
ms = mins * 60
tot = ds + hs + ms + sec
print(tot, "seconds")
