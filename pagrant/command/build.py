"""
Build the environment.
"""

import sys, os
import logging
from subprocess import Popen, PIPE

sys.path.append('../../../')
from pagrant.util.command import Command
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.requirement.manager import Manager as RequirementManager
from pagrant.helper.file import File as FileHelper

__author__ = 'derek'


class Build(Command):
    """
    Build the ec2 instance.
    """

    def configure(self, parser):
        """
        Override Command.configure
        :param parser: The pagrant util parser
        :return:
        """
        subparsers = parser.get_subprocess({'help': "(help='build)", 'dest': 'command'})
        subprocess_parser = subparsers.add_parser('build', help='Build the environment')
        # subprocess_parser.add_argument('-e', '--env', metavar='env', type=str, nargs=1, help='The project origin to deal with.', default='default')
        # subprocess_parser.add_argument('-v', metavar='verbose', type=str, nargs='?', help='In verbose mode?', default='not_passed')
        return self

    def run(self, args, conf):
        """
        Run the process.
        :param args: Arguments passed via console.
        :param conf: The system configuration.
        :return:
        """
        env_vars = conf.get('build.env_vars')
        env_file = conf.get('build.env_vars_file')
        # print(env_vars)
        req_manager = RequirementManager()
        req_manager.require_once('conf.env_vars', env_vars=env_vars, env_file=env_file)
        # Nginx
        req_manager.require_once('app.nginx')
        req_manager.require_once('conf.nginx', conf=Setting.conf.get('build.nginx.conf'))
        # PHP 5.6
        req_manager.require_once('app.php56', conf=Setting.conf.get('build.php56.app'))
        req_manager.require_once('conf.php56', conf=Setting.conf.get('build.php56.conf'))
        # MySQL 5.6
        req_manager.require_once('app.mysql56', conf=Setting.conf.get('build.mysql56.app'))
        req_manager.require_once('conf.mysql56', conf=Setting.conf.get('build.mysql56.conf'))
        # SSMTP
        req_manager.require_once('app.ssmtp')
        req_manager.require_once('conf.ssmtp', conf=Setting.conf.get('build.ssmtp.conf'))
        # Docker
        req_manager.require_once('app.docker')
        # Composer
        req_manager.require_once('app.composer')
        # Alias pagrant
        FileHelper.write_excl('/root/.bash_aliases', ["alias pagrant='python /vagrant/pagrant/bin/console.py'"], force=True)


def export(parser):
    """
    To export this sub process to pagrant
    :param conf:
    :param parser:
    :return:
    """
    build = Build()
    build.configure(parser)
    return build
