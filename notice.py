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
import time
import json

file = open('files/config.json')
notification = json.load(file)

title = notification['title']
message = notification['message']
voice = notification['voice']
notice = notification['time']

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

while True:
    time.sleep(30)
