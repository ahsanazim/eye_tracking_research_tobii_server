# Local Websocket Server

Local websocket server that reads gaze data from the Talon local software, then sends it to the chrome extension client.

Specifically:

***PRIMARY:***

`server.py`
* reads user gaze coordinate data from `talon.log` file
* cleans the data
* records it in the `data.txt` log file
* sends it to the client

***SECONDARY:***

`plot_data.py`
* uses `matplotlib` library to plot the saved data

`data*.txt`
* all log files that contain recorded data

`test.py`
* testing out various functions, not active