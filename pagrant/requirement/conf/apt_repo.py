"""
Application Requirement
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.requirement.conf.base import Base as BaseConfRequirement
from pagrant.helper.command import Command as CommandHelper

__author__ = 'derek'


class AptRepo(BaseConfRequirement):
    """
    Environment variables.
    """

    def configure(self):
        """
        Add apt-get repositories.
        :return:
        """
        # Add Nginx repo.
        CommandHelper.pipe_thru(['wget', '-O', '-', 'https://packagecloud.io/gpg.key'], ['apt-key', 'add', '-'])
        CommandHelper.pipe_thru(['echo', 'deb http://packages.blackfire.io/debian any main'], ['tee', '/etc/apt/sources.list.d/nginx.list'])