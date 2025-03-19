import urllib.request
import json
import math

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    ref = my_request.read()
    data = json.loads(ref)
    result = []
    for item in data :
        if item["enabled"] == True:
            result.append((item["fullName"],item["name"],item["year"],sum(item["exercises"])))
    return result

def retrieve_course(course_name: str):
    req = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    reff = req.read()
    d = json.loads(reff)
    std = []
    hours = []
    ex = []
    k = []
    for key, value in d.items():
        std.append(value["students"])
        hours.append(value["hour_total"])
        ex.append(value["exercise_total"])
        k.append(key)

    my_dict = {}
    my_dict["weeks"] = len(k)
    my_dict["students"] = max(std)
    my_dict["hours"] = sum(hours)
    my_dict["hours_average"] = math.floor(my_dict["hours"]/my_dict["students"])
    my_dict["exercises"] = sum(ex)
    my_dict["exercises_average"] = math.floor(my_dict["exercises"]/my_dict["students"])

    return my_dict
    
if __name__ == "__main__":
    retrieve_all()
    retrieve_course("docker2019")