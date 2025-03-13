from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
birth = datetime(year,month,day)
m = datetime(1999,12,31)
difference = m - birth
if difference.days > 0 :
    msg = f"You were {difference.days} days old on the eve of the new millennium."
elif difference.days < 0 :
    msg = f"You weren't born yet on the eve of the new millennium."
print(msg) 

