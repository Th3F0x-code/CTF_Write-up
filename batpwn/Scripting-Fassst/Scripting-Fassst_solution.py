from datetime import datetime, timezone
from websocket import create_connection

# create a connection to the server
ws = create_connection("ws://challenges.ctfd.io:30065/")
print(ws.recv())
ws.send("y")  # send "yes" to the server to start the challenge
while True:  # start an infinite loop
    a = ws.recv()  # receives the string-date
    print(a)  # print the date
    dt = datetime.strptime(a, "%Y-%m-%d %H:%M:%S")  # try to format the date into this form
    # send the formatted date to the server and if it is wrong we have found the flag
    ws.send(str(int(dt.replace(tzinfo=timezone.utc).timestamp())))
