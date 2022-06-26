import datetime
import json


with open("acdc.json") as jsonFile:
    acdc = json.load(jsonFile)

duration = 0
for track in acdc["album"]["tracks"]["track"]:
    duration_str = track["duration"]
    duration += int(duration_str)

print(duration)

time_ = datetime.timedelta(seconds=duration)
print(time_)

