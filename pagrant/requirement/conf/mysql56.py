"""
Application Requirement
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.requirement.conf.base import Base as BaseConfRequirement
from pagrant.helper.mysql56 import Mysql56 as Mysql56Helper

__author__ = 'derek'


class Mysql56(BaseConfRequirement):
    """
    Environment variables.
    """

    def configure(self, conf={}):
        BaseConfRequirement.map(conf)
        Mysql56Helper.restart()