"""
Command helper
"""

import sys, os, shutil
from subprocess import Popen, PIPE, STDOUT

sys.path.append('../../../')
from pagrant.system import System

__author__ = 'derek'


class Command:
    """
    The command helper.
    """

    @staticmethod
    def pipe_thru(*commands):
        """
        Pipe commands each one to the next.
        :param commands: The commands to pipe through
        :return:
        """
        if commands is not None:
            last_process = None
            for command in commands:
                if last_process is None:
                    last_process = Popen(command, stdout=PIPE, stderr=PIPE)
                else:
                    last_process = Popen(command, stdin=last_process.stdout, stdout=PIPE, stderr=PIPE)
            System.log_subprocess_output(last_process)

    @staticmethod
    def run(command, params={}):
        """
        Run command in bash and log the output.
        :param command: The command to run.
        :param params: The parameters to pass to Popen.
        :return:
        """
        pass_params = {'stdout': PIPE, 'stderr': PIPE}
        pass_params.update(params)
        process = Popen(command, **pass_params)
        System.log_subprocess_output(process)

    @staticmethod
    def add_user(user, uid):
        """
        Create the user with uid if provided.
        :param user: The user to create.
        :param uid: The user id to come with.
        :return:
        """
        if uid:
            command = ['useradd', '-u', uid, user]
        else:
            command = ['useradd', user]
        Command.run(command)

    @staticmethod
    def add_user_to_group(user, group):
        """
        Add the user to group.
        :param user: The user to change.
        :param group: The group to add to.
        :return:
        """
        Command.run(['usermod', '-a', '-G', user, group])




