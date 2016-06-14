"""
Php56 helper
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.helper.command import Command as CommandHelper
from pagrant.helper.apt import Apt as AptHelper

__author__ = 'derek'


class Php56:
    """
    The php helper.
    """

    @staticmethod
    def install(conf={}):
        """
        Install php.
        :param conf: Possible configurations.
        :return:
        """
        AptHelper.update()
        AptHelper.add_repo('ppa:ondrej/php5-5.6')
        AptHelper.update()
        packages = ['php5', 'php5-fpm']
        if conf['packages']:
            packages = conf['packages']
        AptHelper.install(packages)

    @staticmethod
    def start():
        CommandHelper.run(['service', 'php5-fpm', 'start'])

    @staticmethod
    def restart():
        CommandHelper.run(['service', 'php5-fpm', 'restart'])