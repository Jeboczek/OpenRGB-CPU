import sys
import psutil
from typing import Optional
from openrgb import OpenRGBClient
from openrgb.orgb import Device
from openrgb.utils import RGBColor, DeviceType

from config.config import Config

class OpenRGBCPU:
    def __init__(self) -> None:
        self.client : Optional[OpenRGBClient] = None
        self.config : Optional[Config] = None
        self.device : Optional[Device] = None


    def connect(self):
        """Connect to OpenRGB server"""
        self.config = Config() 
        self.client = OpenRGBClient(address=self.config.server_IP, port=self.config.server_port)
        
        try:
            if self.config.device_name is None:
                raise IndexError()
            self.device = [device for device in self.client.devices if device.name.lower() == self.config.device_name.lower()][0]
        except IndexError:
            self._show_error_with_no_selected_device()
        
        print("Connected")


    def _show_error_with_no_selected_device(self):
        """This error will be shown if user don't provide device name in env variable."""
        print("ERR: You need specify device in DEVICE_NAME env variable.")
        print("List of Devices:")
        for device in self.client.devices:
            print(f"{device.name}\t{device.type.name}")
        sys.exit(-1)


    def update_color(self, cpu_measure_time : int = 0.5):
        if self.connect is None:
            print("You need to connect first")
        else:
            cpu_percent = psutil.cpu_percent(cpu_measure_time)
            self.device.set_color(RGBColor.fromHSV(self.config.color_hue, 70, cpu_percent))

    def disconnect(self):
        self.client.disconnect()
        self.client = None
