import os
from typing import Optional

class Config:
    def __init__(self) -> None:
        self.serverIP : str = "127.0.0.1"
        self.serverPort : int = 6742
        self._load_from_env()

    def _load_from_env(self):
        # Get IP 
        ip = os.environ.get("IP")
        self.serverIP = self.serverIP if ip is None else ip

        # Get Port
        port = os.environ.get("PORT")
        self.serverPort = self.serverPort if port is None else int(port)

