"""
Composer helper
"""

import sys, os, stat
from subprocess import Popen, PIPE

sys.path.append('../../../')
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.helper.command import Command as CommandHelper

__author__ = 'derek'


class Composer:
    """
    The composer helper.
    """

    @staticmethod
    def install(conf={}):
        """
        Install composer.
        :param conf: Possible configurations.
        :return:
        """
        CommandHelper.pipe_thru(['curl', '-sS', 'https://getcomposer.org/installer'], ['php', '--', '--install-dir=/usr/local/bin', '--filename=composer'])