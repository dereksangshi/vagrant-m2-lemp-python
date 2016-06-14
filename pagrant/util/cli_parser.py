#!/usr/bin/env python

# Import system modules.
import argparse
import sys

# Import the baws package.
sys.path.append('../../')
# from baws import *


class CliParser:
    """
    CliParser class.
    """
    parser = None
    subparsers = None
    opts = {}

    def __init__(self, opts={}):
        """
        Constructor.
        :param opts: The options (should be a dictionary).
        :return:
        """
        if isinstance(opts, dict):
            self.opts.update(opts)

    def get_parser(self):
        if self.parser is None:
            self.parser = argparse.ArgumentParser(description='pagrant cli.')
        return self.parser

    def get_subprocess(self, opts={}):
        if self.subparsers is None:
            if not isinstance(opts, dict):
                opts = {'help': "(help='sub-command help')", 'dest': 'subprocess'}
            self.subparsers = self.get_parser().add_subparsers(**opts)
        return self.subparsers