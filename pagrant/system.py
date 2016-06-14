import os
import pprint
import logging
import string


class System:
    """
    Package kernel.
    """
    sys_base_dir = None

    @staticmethod
    def assist(dictionary, die=True):
        # print(json.dumps(dictionary, indent=2))
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(dictionary)
        if die is True:
            exit(0)

    @staticmethod
    def base_dir():
        if System.sys_base_dir is None:
            System.sys_base_dir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
        return System.sys_base_dir

    @staticmethod
    def dir(sub_dir=''):
        return '%s/%s' % (System.base_dir(), sub_dir)

    @staticmethod
    def conf_dir():
        return System.dir('conf')

    @staticmethod
    def bin_dir():
        return System.dir('pagrant/bin')

    @staticmethod
    def util_path():
        return System.dir('pagrant/util')

    @staticmethod
    def pagrant_filename(name, sub_dir=''):
        sub_dir = 'pagrant/%s' % sub_dir
        return System.filename(name, sub_dir)

    @staticmethod
    def filename(name, sub_dir=''):
        return "%s/%s" % (System.dir(sub_dir).rstrip('/'), name)

    @staticmethod
    def abs_path(file):
        if not os.path.isabs(file):
            file = '%s/%s' % (System.base_dir(), file)
        return file

    @staticmethod
    def tag_message(msg, tag):
        return "[%s] %s" % (tag, msg)

    @staticmethod
    def err_std_out(msg):
        # os.system('echo "%s[ERROR] %s%s"' % ('\033[0;31m', msg.replace('"', '\\"'), '\033[0m'))
        os.system('echo "%s"' % (System.tag_message(msg, 'ERROR').replace('"', '\\"')))

    @staticmethod
    def msg_std_out(msg):
        # os.system('echo "%s%s%s"' % ('\033[1;32m', msg.replace('"', '\\"'), '\033[0m'))
        os.system('echo "%s"' % (msg.replace('"', '\\"')))

    @staticmethod
    def std_out(msg):
        print(msg)

    @staticmethod
    def open_file(filename, mode='a+'):
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        return open(filename, mode)

    @staticmethod
    def log_info(msg):
        logging.info(msg)

    @staticmethod
    def log_subprocess_output(process):
        System.log_info('|'.join(process.communicate()))

    @staticmethod
    def underscore_to_class(underscore_str):
        return string.capwords(underscore_str.replace('_', ' ')).replace(' ', '')


cd = System.dir
