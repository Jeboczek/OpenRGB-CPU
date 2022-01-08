import os
from unittest import TestCase, mock
from config.config import Config

class TestConfig(TestCase):
    @mock.patch.dict(os.environ, {"IP": "111.111.111.111"})
    def test_config_ip(self):
        conf = Config()
        self.assertEqual(conf.serverIP, "111.111.111.111")

    @mock.patch.dict(os.environ, {"PORT": "11111"})
    def test_config_port(self):
        conf = Config()
        self.assertEqual(conf.serverPort, 11111)