"""
Composer Application Requirement
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.requirement.app.base import Base as BaseAppRequirement
from pagrant.helper.composer import Composer as ComposerHelper

__author__ = 'derek'


class Composer(BaseAppRequirement):
    """
    Composer compose.
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
        Install Composer
        :param conf:
        :return:
        """
        ComposerHelper.install()
