"""
Application Requirement
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.requirement.conf.base import Base as BaseConfRequirement
from pagrant.helper.php56 import Php56 as Php56Helper

__author__ = 'derek'


class Php56(BaseConfRequirement):
    """
    Environment variables.
    """

    def configure(self, conf={}):
        BaseConfRequirement.map(conf)
        Php56Helper.restart()