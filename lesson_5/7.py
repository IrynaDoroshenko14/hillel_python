import datetime


def is_date(day, month, year):
    date = f"{day}{month}{year}"
    try:
        datetime.datetime.strptime(date, "%d%m%Y")
    except:
        return "wrong date"

    return "correct date"


print(is_date("29", "02", "2020"))
print(is_date("30", "02", "2022"))
