import datetime
import json

file = "acdc.json"


def get_total_duration(file_name):
    with open(file_name) as jsonFile:
        acdc = json.load(jsonFile)

    duration = 0
    for track in acdc["album"]["tracks"]["track"]:
        duration_str = track["duration"]
        duration += int(duration_str)
    return duration


duration = get_total_duration(file)
print(duration)


def get_time_for_secs(seconds):
    return datetime.timedelta(seconds=seconds)


time_ = get_time_for_secs(duration)
print(time_)
