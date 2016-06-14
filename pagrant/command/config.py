"""
Config the environment.
"""

import sys, os
import logging
from subprocess import Popen, PIPE

sys.path.append('../../../')
from pagrant.util.command import Command
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.requirement.manager import Manager as RequirementManager
from pagrant.helper.command import Command as CommandHelper

__author__ = 'derek'


class Config(Command):
    """
    Config the ec2 instance.
    """

    def configure(self, parser):
        """
        Override Command.configure
        :param parser: The pagrant util parser
        :return:
        """
        subparsers = parser.get_subprocess({'help': "(help='config)", 'dest': 'command'})
        subprocess_parser = subparsers.add_parser('config', help='Config the environment')
        subprocess_parser.add_argument('-a', '--app', metavar='app', type=str, nargs='?', help='The application to re-config.', default='all')
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
        if args['app'] == 'all':
            req_manager.require_once('conf.nginx', conf=Setting.conf.get('build.nginx.conf'))
            req_manager.require_once('conf.php56', conf=Setting.conf.get('build.php56.conf'))
            req_manager.require_once('conf.mysql56', conf=Setting.conf.get('build.mysql56.conf'))
        elif args['app'] == 'php':
            req_manager.require_once('conf.php56', conf=Setting.conf.get('build.php56.conf'))
        elif args['app'] == 'nginx':
            req_manager.require_once('conf.nginx', conf=Setting.conf.get('build.nginx.conf'))
        elif args['app'] == 'mysql':
            req_manager.require_once('conf.mysql56', conf=Setting.conf.get('build.mysql56.conf'))


def export(parser):
    """
    To export this sub process to pagrant
    :param conf:
    :param parser:
    :return:
    """
    config = Config()
    config.configure(parser)
    return config
