"""
Ssmtp helper
"""

import sys, os, stat
from subprocess import Popen, PIPE

sys.path.append('../../../')
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.helper.command import Command as CommandHelper
from pagrant.helper.apt import Apt as AptHelper

__author__ = 'derek'


class Ssmtp:
    """
    The ssmtp helper.
    """

    @staticmethod
    def install(conf={}):
        """
        Install ssmtp.
        :param conf: Possible configurations.
        :return:
        """
        # Install the package
        AptHelper.install('mailutils')
        AptHelper.install('ssmtp')