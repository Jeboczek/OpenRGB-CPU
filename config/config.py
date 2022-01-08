import os
from typing import Optional

class Config:
    def __init__(self) -> None:
        self.server_IP : str = "127.0.0.1"
        self.server_port : int = 6742
        self.device_name : Optional[str] = None
        self._load_from_env()

    def _load_from_env(self):
        # Get IP 
        ip = os.environ.get("IP")
        self.server_IP = self.server_IP if ip is None else ip

        # Get port
        port = os.environ.get("PORT")
        self.server_port = self.server_port if port is None else int(port)

        # Get device name
        device_name = os.environ.get("DEVICE_NAME")
        self.device_name = device_name

