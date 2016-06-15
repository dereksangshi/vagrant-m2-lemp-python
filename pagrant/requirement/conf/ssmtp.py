"""
Application Requirement
"""

import sys

sys.path.append('../../../')
from pagrant.system import System
from pagrant.requirement.conf.base import Base as BaseConfRequirement
from pagrant.helper.ssmtp import Ssmtp as SsmtpHelper

__author__ = 'derek'


class Ssmtp(BaseConfRequirement):
    """
    Environment variables.
    """

    def configure(self, conf={}):
        BaseConfRequirement.map(conf)