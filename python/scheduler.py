import datetime as dt
import sched
import time
from threading import Thread

# Asia/Tokyo
tzinfo = dt.timezone(dt.timedelta(hours=9))

# 1:00 AM
target_time = dt.time(hour=1, minute=0, second=0, microsecond=0, tzinfo=tzinfo)

scheduler = sched.scheduler(time.time, time.sleep)

def hello():
    print("hello")

def schedule():
    while True:
        next_dt = dt.datetime.combine(dt.datetime.now(tzinfo), target_time) + dt.timedelta(days=1)
        scheduler.enterabs(next_dt.timestamp(), 1, hello)
        scheduler.run()

t = Thread(target=schedule, daemon=True)
t.start()
