"""
Mysql56 Application Requirement
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.requirement.app.base import Base as BaseAppRequirement
from pagrant.helper.mysql56 import Mysql56 as Mysql56Helper

__author__ = 'derek'


class Mysql56(BaseAppRequirement):
    """
    Mysql56 compose.
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
        Install Mysql56
        :param conf:
        :return:
        """
        Mysql56Helper.install(conf)