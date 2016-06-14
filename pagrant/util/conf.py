"""
Configuration
"""

import yaml
import copy


class Conf:
    """
    Configuration class.
    """

    def __init__(self, conf_file=None, conf_dict=None, opts={}):
        """
        Constructor.
        :param conf_file: The Yaml configuration file.
        :return:
        """
        self.conf = {}
        self.delimiter = '.'
        self.key_values = {}
        self.opts = {
            'delimiter': '.',
            'open_mode': 'r'
        }
        if isinstance(opts, dict):
            self.opts.update(opts)
        if conf_file is not None:
            self.from_file(conf_file)
        if conf_dict is not None and isinstance(conf_dict, dict):
            self.from_dict(conf_dict)

    def from_file(self, conf_file):
        """
        Load configuration from the given file.
        :param conf_file:
        :return:
        """
        stream = open(conf_file, self.opts['open_mode'])
        self.from_dict(yaml.load(stream))
        stream.close()
        return self

    def from_dict(self, conf_dict):
        """
        Provide the configuration directly.
        :param conf_dict:
        :return:
        """
        self.update(conf_dict)
        return self

    def to_key_values(self):
        """
        Translate conf_tree like dictionary into key-value like dictionary.
        :return:
        """
        self.traverse_into_key_values(self.conf)

    def traverse_into_key_values(self, conf_tree, conf_nodes=[]):
        """
        Traverse the dictionary recursively to form the key-value dictionary.
        :param conf_tree: The tree-like configuration dictionary.
        :param conf_nodes: The nodes list.
        :return:
        """
        for n in conf_tree:
            conf_nodes.append(n)
            if isinstance(conf_tree[n], dict) and len(conf_tree[n]) > 0:
                self.traverse_into_key_values(conf_tree[n], conf_nodes)
            else:
                self.key_values[self.opts['delimiter'].join(conf_nodes)] = conf_tree[n]
            conf_nodes.pop()

    def get_key_values(self):
        """
        Get the key-value like configuration dictionary.
        :return:
        """
        if len(self.key_values) == 0:
            self.to_key_values()
        return self.key_values

    def get_sub_conf_by_conf_nodes(self, conf_tree, conf_nodes):
        """
        Get the sub tree-like configuration dictionary by the given nodes.
        :param conf_tree: The tree-like configuration dictionary.
        :param conf_nodes: The nodes list.
        :return:
        """
        if isinstance(conf_tree, dict) is False:
            return
        else:
            current_node = conf_nodes.pop(0)
            # if current_node not in conf_tree:
            #     raise KeyError
            if len(conf_nodes) > 0:
                return self.get_sub_conf_by_conf_nodes(conf_tree[current_node], conf_nodes)
            else:
                return conf_tree[current_node]

    def path_to_conf_nodes(self, path=''):
        """
        Convert the path(string) into nodes(list).
        :param path: The path (e.g. 'sub_processes.s3.actions')
        :return:
        """
        path = path.strip(self.opts['delimiter'])
        if len(path) == 0:
            return []
        return path.split(self.opts['delimiter'])

    def get(self, path=''):
        """
        Get the sub configuration dictionary of the path.
        :param path: The path (e.g. 'sub_processes.s3.actions')
        :return:
        """
        if path == '':
            return self.conf
        return self.get_sub_conf_by_conf_nodes(self.conf, self.path_to_conf_nodes(path))

    def update(self, dictionary={}):
        """
        Update self.conf with the given dictionary.
        """
        if not isinstance(dictionary, dict):
            return
        self.conf = self.deep_merge(self.conf, dictionary)

    def deep_merge(self, a, b):
        """
        Deep merge 2 dictionaries.
        """
        if not isinstance(b, dict):
            return b
        result = copy.deepcopy(a)
        for k, v in b.items():
            if k in result and isinstance(result[k], dict):
                result[k] = self.deep_merge(result[k], v)
            else:
                result[k] = copy.deepcopy(v)
        return result
