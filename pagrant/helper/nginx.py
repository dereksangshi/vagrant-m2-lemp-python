"""
Nginx helper
"""

import sys, os, stat
from subprocess import Popen, PIPE

sys.path.append('../../../')
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.helper.command import Command as CommandHelper
from pagrant.helper.apt import Apt as AptHelper

__author__ = 'derek'


class Nginx:
    """
    The nginx helper.
    """

    @staticmethod
    def install(conf={}):
        """
        Install nginx.
        :param conf: Possible configurations.
        :return:
        """
        # os.chmod(repo_file, stat.S_IRUSR + stat.S_IWUSR + stat.S_IXUSR + stat.S_IRGRP + stat.S_IXGRP + stat.S_IROTH + stat.S_IXOTH)
        # Add Nginx repo.
        CommandHelper.pipe_thru(['curl', 'http://nginx.org/keys/nginx_signing.key'], ['apt-key', 'add', '-'])
        lines = [
            '#[Nginx]',
            'deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx',
            'deb-src http://nginx.org/packages/mainline/ubuntu/ trusty nginx'
        ]
        AptHelper.add_src(lines)
        AptHelper.update()
        # Remove any existing nginx-common
        AptHelper.remove(['nginx-*', 'nginx'])
        # Install the package
        AptHelper.install('nginx')

    @staticmethod
    def start(args={}):
        CommandHelper.run(['service', 'nginx', 'start'])

    @staticmethod
    def restart(args={}):
        CommandHelper.run(['service', 'nginx', 'restart'])