"""
Ssmtp Application Requirement
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.requirement.app.base import Base as BaseAppRequirement
from pagrant.helper.ssmtp import Ssmtp as SsmtpHelper

__author__ = 'derek'


class Ssmtp(BaseAppRequirement):
    """
    Ssmtp compose.
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
        Install Ssmtp
        :param conf:
        :return:
        """
        SsmtpHelper.install()
