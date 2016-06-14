"""
Commands
"""

import sys
sys.path.append('../../../')

__author__ = 'derek'


class Command:
    """
    The subprocess abstract class.
    """

    def configure(self, parser):
        """
        The cli commands to export.
        :param parser:
        :return:
        """
        raise NotImplementedError("Each sub process must have a configure method")

    def run(self, args, conf):
        """
        Run the sub process based on the given arguments.
        :param args:
        :param conf:
        :return:
        """
        raise NotImplementedError("Each sub process must have a run method")
