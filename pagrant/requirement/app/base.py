"""
Application Requirement
"""


__author__ = 'derek'


class Base:
    """
    The app requirement base class.
    """

    def exists(self, **kwargs):
        """
        If the application already exists.
        :param kwargs:
        :return:
        """
        raise NotImplementedError("Each application requirement needs to implement the 'exists' method.")

    def install(self, **kwargs):
        """
        Install the application.
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError("Each application requirement needs to implement the 'install' method.")