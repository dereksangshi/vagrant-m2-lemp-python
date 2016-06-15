"""
Docker Application Requirement
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.requirement.app.base import Base as BaseAppRequirement
from pagrant.helper.docker import Docker as DockerHelper

__author__ = 'derek'


class Docker(BaseAppRequirement):
    """
    Docker compose.
    """

    def exists(self, conf={}):
        """
        If the application already exists.
        :param conf:
        :return:
        """
        return False;

    def install(self, conf={}):
        """
        Install Docker
        :param conf:
        :return:
        """
        DockerHelper.install()
