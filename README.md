# OpenRGB-CPU
Highlight your leds relative to CPU usage.
![Showcase](github/showcase.gif)
## How to install?
### Linux
After cloning project from github.
```
git clone https://github.com/Jeboczek/OpenRGB-CPU
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
You need have OpenRGB server installed in your distribution, if server exists in your installation you can run server by executing
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
| COLOR_HUE            | Hue of your color from HSV.                                                                                                                     |
| IP                   | IP of your OpenRGB server instance.                                                                                                             |
| PORT                 | Port of your OpenRGB server instance.                                                                                                           |