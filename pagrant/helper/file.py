"""
File helper
"""

import sys, os, shutil

sys.path.append('../../../')
from pagrant.system import System

__author__ = 'derek'


class File:
    """
    The file helper.
    """

    @staticmethod
    def map_files(src, dst):
        """
        Map files from src to files dst one by one.
        :param src: Source directory or filename
        :param dst: Destination directory or filename
        :return:
        """
        file_to_file_mappings = {}
        # Traverse all the file from src if it's a directory.
        if os.path.isdir(src):
            for (path, a, files) in os.walk(src):
                for f in files:
                    src_filename = os.path.join(path, f)
                    # The destination is a directory.
                    if os.path.isdir(dst):
                        dst_dir = os.path.join(dst, path.replace(src, '').lstrip(os.sep))
                        # Create destination directory path.
                        if not os.path.exists(dst_dir):
                            os.makedirs(dst_dir)
                        dst_filename = os.path.join(dst_dir, f)
                    else:
                        dst_filename = dst
                    file_to_file_mappings[src_filename] = dst_filename
        else:
            if os.path.isdir(dst):
                if not os.path.exists(dst):
                    os.makedirs(dst)
                dst_filename = os.path.join(dst, os.path.basename(src))
            else:
                dst_filename = dst
            file_to_file_mappings[src] = dst_filename
        return file_to_file_mappings

    @staticmethod
    def map_copy(file_to_file_mappings, replacements={}, pattern='{{*}}'):
        """
        Copy files based on file to file mappings
        :param file_to_file_mappings: Dictionary with source file to destination file one by one.
        :param replacements:
        :param pattern:
        :return:
        """
        if isinstance(file_to_file_mappings, dict):
            for src_f in file_to_file_mappings:
                if os.path.isfile(src_f):
                    if replacements:
                        with open(src_f, 'r') as file :
                            new_content = File.compile(file.read(), replacements, pattern)
                            with open(file_to_file_mappings[src_f], 'w') as dst_file:
                                dst_file.write(new_content)
                    else:
                        shutil.copy(src_f, file_to_file_mappings[src_f])

    @staticmethod
    def compile(content, replacements={}, pattern='{{*}}'):
        """
        Compile the content.
        :param content: The content to compile.
        :param replacements: The replacements to run through
        :param pattern: The pattern for the key work mapping
        :return:
        """
        for param in replacements:
            str_to_replace = pattern.replace('*', param)
            content = content.replace(str_to_replace, replacements[param])
        return content

    @staticmethod
    def copy(src, dst, replacements={}, pattern='{{*}}'):
        """
        Copy files from src to dst
        :param src: Source directory or filename
        :param dst: Destination directory or filename
        :param replacements:
        :param pattern:
        :return:
        """
        File.map_copy(File.map_files(src, dst), replacements, pattern)

    @staticmethod
    def map_by_mappings(mappings, replacements, pattern):
        """
        Directory mappings:
        :param mappings: A directory with src => dst (either files to files or dirs to dirs).
        :param replacements: The key words to replace.
        :param pattern: The pattern of the key words in src.
        :return:
        """
        if not isinstance(mappings, dict) or not mappings:
            return
        extra_params = {}
        if isinstance(replacements, dict) and replacements:
            extra_params['replacements'] = replacements
        if pattern:
            extra_params['pattern'] = pattern
        for src in mappings:
            File.copy(src, mappings[src], **extra_params)

    @staticmethod
    def write_excl(file, lines, key_words=None, force=False):
        """
        Write lines into the file if key words not exist.
        :param file: Name of the file to write to.
        :param lines: List of lines to write or a string of a single line.
        :param key_words: List of key words to check or a string of a single key word.
        :param force: True for creating the file if not exists.
        :return:
        """
        if force and not os.path.isfile(file):
            f = open(file, 'w+')
            f.close()
        if os.path.isfile(file):
            f = System.open_file(file, 'a+')
            content = f.read()
            # Only check if the given keyword exists before writing given lines.
            if key_words is not None:
                exists = False
                key_words = key_words if isinstance(key_words, list) else [key_words]
                for val in key_words:
                    if val in content:
                        exists = True
                        break
                if not exists:
                    lines = lines if isinstance(lines, list) else [lines]
                    for line in lines:
                        f.write(line+'\n')
            # If no keyword is given, check if each line exists before writing.
            else:
                lines = lines if isinstance(lines, list) else [lines]
                for line in lines:
                    if line not in content:
                        f.write(line+'\n')
            f.close()
