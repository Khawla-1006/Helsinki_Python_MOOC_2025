# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str) :
    station_data = {}
    with open(filename) as data :
        for line in data :
            s = line.replace("\n","")
            stations = s.split(";")
            if stations[0] == "Longitude" :
                continue
            station_data[stations[3]] = (float(stations[0]),float(stations[1]))
    return station_data

def distance(stations: dict, station1: str, station2: str) :
    import math
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict) :
    #greatest
    print()

if __name__ == "__main__" :
    stations = get_station_data("stations1.csv")
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)