import logging, os, re

from pagrant.util.conf import Conf
from pagrant.system import System


class Setting:
    """
    Initializer
    """
    conf = Conf()
    param = Conf()

    @staticmethod
    def include(setting_file):
        """
        Update the system setting.
        :param setting_file: A python setting file to include.
        :return:
        """
        if os.path.isfile(setting_file):
            with open(setting_file) as f:
                code = compile(f.read(), setting_file, 'exec')
                exec(code)

    @staticmethod
    def apply():
        Setting.configure_logging()

    @staticmethod
    def configure_logging():
        """
        Configure the logging.
        :param cus_conf: The config dictionary to use.
        :return: None
        """
        conf = Setting.conf.get('logging')
        logging.basicConfig(**conf)


param = Setting.param
conf = Setting.conf


def sp(name):
    return param.get(name)

# Default system settings.
conf.update({
    'logging': {
        'format': '[%(asctime)s] <%(levelname)s> %(message)s',
        'datefmt': '%Y/%m/%d %I:%M:%S',
        'filename': System.dir('/var/pagrant.log'),
        'level': logging.DEBUG
    }
})
