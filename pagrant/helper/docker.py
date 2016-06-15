"""
Docker helper
"""

import sys, os, stat
from subprocess import Popen, PIPE

sys.path.append('../../../')
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.helper.command import Command as CommandHelper
from pagrant.helper.apt import Apt as AptHelper

__author__ = 'derek'


class Docker:
    """
    The docker helper.
    """

    @staticmethod
    def install(conf={}):
        """
        Install docker.
        :param conf: Possible configurations.
        :return:
        """
        AptHelper.update()
        AptHelper.install(['apt-transport-https', 'ca-certificates'])
        CommandHelper.run(['apt-key', 'adv', '--keyserver', 'hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D'])
        lines = [
            '#[Docker]',
            'deb https://apt.dockerproject.org/repo ubuntu-trusty main'
        ]
        AptHelper.add_src(lines)
        AptHelper.update()
        # Purge old repo if exists
        AptHelper.purge(['lxc-docker'])
        CommandHelper.run(['apt-cache', 'policy', 'docker-engine'])
        # Install the package
        AptHelper.update()
        AptHelper.install('docker-engine')

    @staticmethod
    def start(args={}):
        CommandHelper.run(['service', 'docker', 'start'])

    @staticmethod
    def restart(args={}):
        CommandHelper.run(['service', 'docker', 'restart'])