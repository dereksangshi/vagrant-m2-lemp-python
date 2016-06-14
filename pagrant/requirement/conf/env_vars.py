"""
Application Requirement
"""

import sys, os

sys.path.append('../../../')
from pagrant.system import System
from pagrant.requirement.conf.base import Base as BaseConfRequirement

__author__ = 'derek'


class EnvVars(BaseConfRequirement):
    """
    Environment variables.
    """

    def configure(self, env_vars={}, env_file='/etc/profile.d/custom-env-vars.sh'):
        """
        Configure the environment variables.
        Save them all into the file.
        Also update the current shell environment with them.
        :param env_vars: Environment variables.
        :param env_file: The file to export environment variables.
        :return:
        """
        # Remove the env file if it exists.
        if os.path.isfile(env_file):
            os.remove(env_file)
        if isinstance(env_vars, dict):
            file = System.open_file(env_file, 'a+')
            file.write("#!/usr/bin/env bash\n")
            for var_name in env_vars:
                file.write("export %s=%s\n" % (var_name, env_vars[var_name]))
                os.environ[var_name] = env_vars[var_name]
            file.close()