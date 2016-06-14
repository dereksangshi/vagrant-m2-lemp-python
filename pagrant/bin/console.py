#!/usr/bin/env python

# Import system modules.
import importlib
import os
import re
import sys
import logging

# Import the pagrant package.
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')
from pagrant.system import System
from pagrant.setting import Setting
from pagrant.util.cli_parser import CliParser


class Console:
    """
    The console to use.
    """

    def __init__(self):
        """
        Constructor.
        :param opts: The options (should be a dictionary).
        :return:
        """
        self.console_parser = None
        self.command = None
        self.command_collection = {}

    def get_console_parser(self):
        """
        Lazy load the parser.
        :return:
        """
        if self.console_parser is None:
            self.init_console_parser()
        return self.console_parser

    def init_console_parser(self):
        """
        Init the parser.
        :return:
        """
        self.console_parser = CliParser()
        self.console_parser.get_parser().add_argument('-s', '--setting-file', metavar='setting_file', type=str, nargs='?', help='The config file.')

    def get_command_name(self):
        """
        Get the sub process name (e.g. s3)
        :return: None|str
        """
        command_name = None
        sys_args = sys.argv
        command_place_holder = False
        for arg in sys_args:
            if command_place_holder is True:
                command_name = arg
                break
            if arg == 'console':
                command_place_holder = True
        return command_name

    def configure_commands(self):
        """
        Loop through 'command' folder and let all the sub processes to configure.
        :return:
        """
        for (path, a, files) in os.walk(System.dir('pagrant/command')):
            # Loop through the directory and get the file names (including the path)
            for f in files:
                filename = os.path.join(path, f)
                match = re.search('^.+/([a-zA-Z0-9_]+).py$', filename)
                try:
                    command_name = match.group(1)
                    if command_name is not None and command_name != '__init__':
                        command = importlib.import_module('pagrant.command.%s' % (command_name))
                        self.command_collection[command_name] = command.export(self.get_console_parser())
                except AttributeError:
                    continue

    def run(self):
        """
        Run sub processes (sub commands).
        :return:
        """
        self.configure_commands()
        args = self.get_console_parser().get_parser().parse_args()
        args = vars(args)
        if args['setting_file'] is None:
            args['setting_file'] = System.filename('setting.py')
        Setting.include(args['setting_file'])
        # Apply the system settings.
        Setting.apply()
        # Run the command.
        if 'command' in args and args['command'] is not None:
            self.command_collection[args['command']].run(args, Setting.conf)

# Process the command.
if __name__ == '__main__':
    try:
        console = Console()
        console.run()
    except SystemExit:
        print('Exit')
    except:
        System.err_std_out(str(sys.exc_info()))
