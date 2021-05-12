import subprocess
import json

file = open('files/config.json')
notification = json.load(file)

title = notification['title']
message = notification['message']

subprocess.run(['osascript', '-e', f'display notification "{message}" with title "{title}"'])
subprocess.run(['osascript', '-e', f'say "{message}"'])
