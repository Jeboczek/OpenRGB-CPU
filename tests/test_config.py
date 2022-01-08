import os
from unittest import TestCase, mock
from config.config import Config

class TestConfig(TestCase):
    @mock.patch.dict(os.environ, {"IP": "111.111.111.111"})
    def test_config_ip(self):
        conf = Config()
        self.assertEqual(conf.server_IP, "111.111.111.111")

    @mock.patch.dict(os.environ, {"PORT": "11111"})
    def test_config_port(self):
        conf = Config()
        self.assertEqual(conf.server_port, 11111)

    @mock.patch.dict(os.environ, {"DEVICE_NAME": "TEST_DEVICE"})
    def test_config_device_name(self):
        conf = Config()
        self.assertEqual(conf.device_name, "TEST_DEVICE")

    def test_config_device_name_without_env(self):
        conf = Config()
        self.assertEqual(conf.device_name, None)