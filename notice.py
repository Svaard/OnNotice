import os

title = "Test"
message = "test"
command = "osascript -e \"display notification "{}" with title "{}"\"".format(message, title)

os.system(command)
