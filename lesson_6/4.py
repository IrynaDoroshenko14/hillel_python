import time
from datetime import datetime


def wait(func):
    def wrapper(*args, **kwargs):
        for sec in range(3, 0, -1):
            print(sec)
            time.sleep(1)

        func(*args, **kwargs)
    return wrapper


@wait
def what_time_is_it_now():
    now = datetime.now().strftime("%H:%M")
    print(now)


what_time_is_it_now()
