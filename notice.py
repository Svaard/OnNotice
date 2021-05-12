import subprocess

title = "Test"
message = "test"
subprocess.run(['osascript', '-e', f'display notification "{message}" with title "{title}"'])
