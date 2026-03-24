import json

with open("features.json") as f:
    data = json.load(f)

for car in data:
    if "ADAS" in car["features"]:
        print(car["car"], "has ADAS")
