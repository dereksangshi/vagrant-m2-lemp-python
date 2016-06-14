"""
Blackfire helper
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.helper.command import Command as CommandHelper
from pagrant.helper.apt import Apt as AptHelper
from pagrant.helper.php56 import Php56 as Php56Helper

__author__ = 'derek'


class Blackfire:
    """
    The blackfirex helper.
    """

    @staticmethod
    def install(conf={}):
        """
        Install blackfirex.
        :param conf: Possible configurations.
        :return:
        """
        AptHelper.install(['blackfire-agent', 'blackfire-php'])
        CommandHelper.run(['blackfire-agent', '-register'])

    @staticmethod
    def start():
        CommandHelper.run(['/etc/init.d/blackfire-agent', 'restart'])
        Php56Helper.restart()