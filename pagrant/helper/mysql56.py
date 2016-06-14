"""
Mysql56 helper
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.helper.command import Command as CommandHelper
from pagrant.helper.apt import Apt as AptHelper

__author__ = 'derek'


class Mysql56:
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
        # AptHelper.update()
        # user = conf['user'] if 'user' in conf else 'root'
        password = conf['password'] if 'password' in conf else 'password'
        CommandHelper.pipe_thru(['echo', "mysql-server mysql-server/root_password password {0}".format(password)], ['debconf-set-selections'])
        CommandHelper.pipe_thru(['echo', "mysql-server mysql-server/root_password_again password {0}".format(password)], ['debconf-set-selections'])
        AptHelper.install('mysql-server-5.6')
        # CommandHelper.run(['mysql', '-uroot', '-e', '\'CREATE USER `{0}`@`%` IDENTIFIED BY "{1}";\''.format(user, password)])
        # CommandHelper.run(['mysql', '-uroot', '-e', '"GRANT ALL PRIVILEGES ON *.* TO `{0}`@`%` WITH GRANT OPTION";'.format(user)])

    @staticmethod
    def start():
        CommandHelper.run(['service', 'mysql', 'start'])

    @staticmethod
    def restart():
        CommandHelper.run(['service', 'mysql', 'restart'])