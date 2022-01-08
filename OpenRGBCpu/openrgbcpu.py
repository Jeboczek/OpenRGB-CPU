import sys
from typing import Optional
from openrgb import OpenRGBClient
from openrgb.orgb import Device
from openrgb.utils import RGBColor, DeviceType

from config.config import Config

class OpenRGBCPU:
    def __init__(self) -> None:
        self.client : Optional[OpenRGBClient] = None
        self.device : Optional[Device] = None


    def connect(self):
        """Connect to OpenRGB server"""
        config = Config() 
        self.client = OpenRGBClient(address=config.server_IP, port=config.server_port)
        
        try:
            self.device = [device for device in self.client.devices if device.name == config.device_name][0]
        except IndexError:
            self._show_error_with_no_selected_device()


    def _show_error_with_no_selected_device(self):
        print("ERR: You need specify device in DEVICE_NAME env variable.")
        print("List of Devices:")
        for device in self.client.devices:
            print(f"{device.name}\t{device.type.name}")
        sys.exit(-1)
