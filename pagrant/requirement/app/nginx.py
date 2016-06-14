"""
Nginx Application Requirement
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.requirement.app.base import Base as BaseAppRequirement
from pagrant.helper.nginx import Nginx as NginxHelper

__author__ = 'derek'


class Nginx(BaseAppRequirement):
    """
    Nginx compose.
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
        Install Nginx
        :param conf:
        :return:
        """
        NginxHelper.install()
