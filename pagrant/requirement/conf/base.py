"""
Configuration Requirement
"""

__author__ = 'derek'

import sys

sys.path.append('../../../')
from pagrant.helper.file import File as FileHelper

class Base:
    """
    The app requirement base class.
    """

    def configure(self):
        """
        Configure the server/environment.
        :param conf:
        :return:
        """
        raise NotImplementedError("Each conf requirement needs to implement the 'configure' method.")

    @staticmethod
    def map(params={}):
        """
        Map the configurations based on passed params (which are set in Settings).
        :param params: The params to use.
        :return:
        """
        if 'mappings' not in params or not isinstance(params['mappings'], dict):
            return
        FileHelper.map_by_mappings(
            params['mappings'],
            params['replacements'] if 'replacements' in params else None,
            params['pattern'] if 'pattern' in params else None
        )