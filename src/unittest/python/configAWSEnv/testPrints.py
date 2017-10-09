from mockito import mock, verify
import unittest

from configAWSEnv.config_ec2_env import Config
from mockito.mocking import Mock



# class PrintTest(unittest.TestCase):
    # def test_should_issue_hello_world_message(self):
    #     mock2 = Mock({'instance1'})
    #     conf = Config()
    #     conf.create_aws_url(mock2)
    #     verify(mock2, 'instance1')