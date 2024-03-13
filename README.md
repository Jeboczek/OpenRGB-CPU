# OpenRGB-CPU
Highlight your leds relative to CPU usage.
![Showcase](github/showcase.gif)
## How to install?
### Linux
After cloning project from github.
```
git clone https://github.com/pawl0wski/OpenRGB-CPU
```
You can make Python's virtual env or you can skip this step if you want.
```
python -m virtualenv ./venv
source ./venv/bin/activate
```
Install dependencies from requirements.txt
```
python -m pip install -r requirements.txt
```
You need have an OpenRGB server installed in your distribution, if a server exists in your installation you can run the server by executing
```
openrgb --server
```
Run script with settings provided in env's
```
ENV DEVICE_NAME="<your_device_name>" COLOR_HUE="210" python main.py
```

## Settings
| Environment Variable | Description                                                                                                                                     |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| DEVICE_NAME          | The name of the device that the program should manipulate the LEDs. The list of devices can be obtained by running the script without settings. |
| COLOR_HUE            | Hue of your color from HSV. Default 350 (red)                                                                                                                     |
| IP                   | IP of your OpenRGB server instance. Default localhost                                                                                                             |
| PORT                 | Port of your OpenRGB server instance. Default 6742                                                                                                           |
