"""
Apt helper
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.helper.command import Command as CommandHelper
from pagrant.helper.file import File as FileHelper

__author__ = 'derek'


class Apt:
    """
    The apt helper.
    """

    @staticmethod
    def update():
        """
        Update apt-get.
        :return:
        """
        CommandHelper.run(['apt-get', '-y', 'update'])

    @staticmethod
    def install(package):
        """
        Install package(s).
        :param package: The package(s) to install. List or string.
        :return:
        """
        # Install the package(s)
        CommandHelper.run(['apt-get', '-y', 'install'] + (package if isinstance(package, list) else [package]))

    @staticmethod
    def remove(package):
        """
        Remove package(s).
        :param package: The package(s) to remove. List or string.
        :return:
        """
        # Install the package(s)
        package = package if isinstance(package, list) else [package]
        for p in package:
            CommandHelper.run(['apt-get', '-y', 'remove', p])

    @staticmethod
    def purge(package):
        """
        Remove package(s).
        :param package: The package(s) to purge. List or string.
        :return:
        """
        # Install the package(s)
        package = package if isinstance(package, list) else [package]
        for p in package:
            CommandHelper.run(['apt-get', 'purge', p])

    @staticmethod
    def add_repo(repo):
        """
        Add repository
        :param repo: The repository(s) to add. List or string.
        :return:
        """
        repo = repo if isinstance(repo, list) else [repo]
        for r in repo:
            CommandHelper.run(['add-apt-repository', r])

    @staticmethod
    def add_src(lines):
        FileHelper.write_excl('/etc/apt/sources.list', lines)