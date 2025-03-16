from datetime import datetime,timedelta

file_name = input("Filename: ")
start_date = input("Starting date: ")
period = input("How many days: ")
print("Please type in screen time in minutes on each day (TV computer mobile): ")

parse_start_date = datetime.strptime(start_date, "%d.%m.%Y")
one_day_plus = timedelta(days=1)


screen_time = {}
day = parse_start_date
for i in range(int(period)):
    nd = datetime.strftime(day,"%d.%m.%Y")
    screen_time[nd] = input(f"Screen time {nd}:")
    day += one_day_plus

days = []
duration = []
for key, value in screen_time.items():
    days.append(key)
    time_in_day = value.split(" ")
    for t in time_in_day :
        duration.append(int(t))
  
time = f"{days[0]}-{days[-1]}"
total = sum(duration)
average = float(total / int(period))


with open(file_name, "w") as ref :
    ref.write(f"Time period: {time}\n")
    ref.write(f"Total minutes: {total}\n")
    ref.write(f"Average minutes: {average}\n")
    for key, value in screen_time.items():
        n = value.replace(" ","/")
        ref.write(f"{key}: {n}\n")

print(f"Data stored in file {file_name}")

