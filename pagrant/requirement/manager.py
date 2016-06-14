"""
Requirement Manager
"""

import sys, importlib, string
from subprocess import Popen, PIPE
import logging

sys.path.append('../../../')
from pagrant.system import System
from pagrant.requirement.app.base import Base as BaseAppRequirement
from pagrant.requirement.conf.base import Base as BaseConfRequirement

__author__ = 'derek'


class Manager():
    """
    Requirement manager.
    """

    def __init__(self):
        """
        Constructor.
        :param opts: The options (should be a dictionary).
        :return:
        """
        self.requirement_container = {}

    @staticmethod
    def get_requirement_instance(requirement_category, requirement_name):
        """
        Get the requirment instance based on its category and name.
        :param requirement_category: The category of the requirement (e.g. 'app').
        :param requirement_name: The name of the requirement (e.g. 'docker_compose').
        :return:
        """
        requirement_module = importlib.import_module('pagrant.requirement.%s.%s' % (requirement_category, requirement_name))
        requirement_class = System.underscore_to_class(requirement_name)
        return getattr(requirement_module, requirement_class)()

    def require_once(self, requirement_key, **kwargs):
        """
        Include the requirement only once.
        :param requirement_key: Key of the requirement (e.g. 'app.docker_composer')
        :param kwargs: Other key word arguments needed by the real requirement.
        :return:
        """
        if requirement_key in self.requirement_container:
            return self
        self.require(requirement_key, **kwargs)

    def require(self, requirement_key, **kwargs):
        """
        Include the requirement.
        :param requirement_key: Key of the requirement (e.g. 'app.docker_composer')
        :param kwargs: Other key word arguments needed by the real requirement.
        :return:
        """
        requirement_name = requirement_key[(requirement_key.find('.') + 1):]
        if 'app.' in requirement_key:
            self.requirement_container[requirement_key] = self.load_app(requirement_name, **kwargs)
        if 'conf.' in requirement_key:
            self.requirement_container[requirement_key] = self.load_conf(requirement_name, **kwargs)
        return self

    def load_app(self, app_name, **kwargs):
        """
        Load the application.
        :param app_name: Name of the application (e.g. 'docker_composer')
        :param kwargs: Other key word arguments needed by the real requirement.
        :return:
        """
        requirement_instance = Manager.get_requirement_instance('app', app_name)
        if isinstance(requirement_instance, BaseAppRequirement):
            if not requirement_instance.exists(**kwargs):
                requirement_instance.install(**kwargs)
        return self

    def load_conf(self, conf_name, **kwargs):
        """
        Configure the environment.
        :param conf_name: Name of the configuration.
        :param kwargs: Other key word arguments needed by the real requirement.
        :return:
        """
        requirement_instance = Manager.get_requirement_instance('conf', conf_name)
        if isinstance(requirement_instance, BaseConfRequirement):
            requirement_instance.configure(**kwargs)
        return self
