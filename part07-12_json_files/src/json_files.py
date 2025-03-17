import json

def print_persons(filename:str):
    with open(filename) as my_file :
        data = my_file.read()
        ref = json.loads(data)
        for item in ref :
            print(f"{item["name"]} {item["age"]} years ({", ".join(item['hobbies'])})")

if __name__ == "__main__" :
    print_persons("file3.json")