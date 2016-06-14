"""
Application Requirement
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.requirement.conf.base import Base as BaseConfRequirement
from pagrant.helper.command import Command as CommandHelper

__author__ = 'derek'


class WwwUser(BaseConfRequirement):
    """
    Environment variables.
    """

    def configure(self, uid):
        """
        Create the www user, assign the user id as passed.
        :param uid:
        :return:
        """
        CommandHelper.add_user('www', uid)