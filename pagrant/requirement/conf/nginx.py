"""
Application Requirement
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.requirement.conf.base import Base as BaseConfRequirement
from pagrant.helper.nginx import Nginx as NginxHelper

__author__ = 'derek'


class Nginx(BaseConfRequirement):
    """
    Environment variables.
    """

    def configure(self, conf={}):
        BaseConfRequirement.map(conf)
        NginxHelper.restart()