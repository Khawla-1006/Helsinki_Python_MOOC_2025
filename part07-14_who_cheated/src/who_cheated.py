import csv
from datetime import datetime,timedelta

def start_task(file_name:str):
    start = []
    with open(file_name) as data :
        for line in csv.reader(data,delimiter=";"):
            start.append(line)
    return start
    
def submit_task(file : str):
    s = []
    with open(file) as ref :
        for l in csv.reader(ref,delimiter=";"):
            s.append(l)
    return s

def cheaters():
    cheater = []
    begin = start_task("start_times.csv")
    submit = submit_task("submissions.csv")
    for std in begin :
        for std_submit in submit :
            if std[0] == std_submit[0]:
                start_time = datetime.strptime(std[1],"%H:%M")
                submit_time = datetime.strptime(std_submit[3],"%H:%M") 
                if (submit_time - start_time) > timedelta(hours=3) :
                    if std[0] not in cheater :
                        cheater.append(std[0])
    return cheater

if __name__ == "__main__":
    cheaters()