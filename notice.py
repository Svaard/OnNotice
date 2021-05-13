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
from notifypy import Notify
import subprocess
import platform
import asyncio
import json
import sys

try:
    with open('files/config.json') as config:
        notification = json.load(config)
        title = notification['title']
        message = notification['message']
        if platform.system() == "Darwin":
            voice = notification['voice']
            notice = notification['time']
        if platform.system() == "Windows":
            winNotification = Notify()
            winNotification.title = title
            winNotification.message = message
except FileNotFoundError:
    print("Config file is missing. Create config file to change default settings.")
    title = "Reminder"
    message = "Stand up and stretch for a few minutes."
    if platform.system() == "Darwin":
        voice = "Alex"
        notice = 42

def macNotice():
    subprocess.run(['osascript', '-e', f'display notification "{message}" with title "{title}"'])
    subprocess.run(['osascript', '-e', f'say "{message}" using "{voice}"'])

def winNotice():
    winNotification.send()

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

if platform.system() == "Darwin":
    sched.add_job(macNotice, trigger)
elif platform.system() == "Windows":
    sched.add(winNotice, trigger)
else:
    print("Your platform isn't supported yet.")
    sys.exit()

sched.start()

loop = asyncio.get_event_loop()
try:
    loop.run_forever()
finally:
    loop.close()
