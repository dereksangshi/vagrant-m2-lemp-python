"""
Blackfire Application Requirement
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.requirement.app.base import Base as BaseAppRequirement
from pagrant.helper.nginx import Blackfire as BlackfireHelper

__author__ = 'derek'


class Blackfire(BaseAppRequirement):
    """
    Blackfire compose.
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
        Install Blackfire
        :param conf:
        :return:
        """
        BlackfireHelper.install()
