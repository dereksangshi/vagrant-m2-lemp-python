"""
Php56 Application Requirement
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.requirement.app.base import Base as BaseAppRequirement
from pagrant.helper.php56 import Php56 as Php56Helper

__author__ = 'derek'


class Php56(BaseAppRequirement):
    """
    Php56 compose.
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
        Install Php56
        :param conf:
        :return:
        """
        Php56Helper.install(conf)