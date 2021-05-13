####################################################
#                                                  #
#                 0/\/ /\/0T1(3                    #
#                                                  #
#   It's gonna remind you every hour...or else.    #
#                                                  #
####################################################

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
import subprocess
import asyncio
import json

try:
    with open('files/config.json') as config:
        notification = json.load(config)
        title = notification['title']
        message = notification['message']
        voice = notification['voice']
        notice = notification['time']
except FileNotFoundError:
    print("Config file is missing. Create config file to change default settings.")
    title = "Reminder"
    message = "Stand up and stretch for a few minutes."
    voice = "Alex"
    notice = 42

def macNotice():
    subprocess.run(['osascript', '-e', f'display notification "{message}" with title "{title}"'])
    subprocess.run(['osascript', '-e', f'say "{message}" using "{voice}"'])

sched = BackgroundScheduler(daemon=True)

trigger = OrTrigger([
    CronTrigger(hour=0, minute=notice), 
    CronTrigger(hour=1, minute=notice),
    CronTrigger(hour=2, minute=notice), 
    CronTrigger(hour=3, minute=notice),
    CronTrigger(hour=4, minute=notice), 
    CronTrigger(hour=5, minute=notice),
    CronTrigger(hour=6, minute=notice), 
    CronTrigger(hour=7, minute=notice),
    CronTrigger(hour=8, minute=notice), 
    CronTrigger(hour=9, minute=notice),
    CronTrigger(hour=10, minute=notice), 
    CronTrigger(hour=11, minute=notice),
    CronTrigger(hour=12, minute=notice), 
    CronTrigger(hour=13, minute=notice),
    CronTrigger(hour=14, minute=notice), 
    CronTrigger(hour=15, minute=notice),
    CronTrigger(hour=16, minute=notice), 
    CronTrigger(hour=17, minute=notice),
    CronTrigger(hour=18, minute=notice), 
    CronTrigger(hour=19, minute=notice),
    CronTrigger(hour=20, minute=notice), 
    CronTrigger(hour=21, minute=notice),
    CronTrigger(hour=22, minute=notice), 
    CronTrigger(hour=23, minute=notice)
])

sched.add_job(macNotice, trigger)
sched.start()

loop = asyncio.get_event_loop()
try:
    loop.run_forever()
finally:
    loop.close()
