#  Author Fakhir Khan

import configparser
import os

__all__ = ['ConfigParser']


class ConfigParser:
    def __init__(self, default_keys: dict, config_file: str = 'config.ini', get_new_config: bool = False):
        """
        Custom Wrapper for reading and writing ini files using simple dictionaries
        :param default_keys: dictionary for setting values in the ini file. Key values become the sections
        and corresponding list of values become section keys.
        :param config_file: path or name of the config file to be created.
        :param get_new_config: boolean flag to overwrite the existing file (if possible)
        """
        self.config_file = config_file
        self.get_new_config = get_new_config
        # This should be a dictionary of dictionaries where first level keys should be the section names and second
        # level keys should be the default keys of the respective section
        self.default_values_in_sections = default_keys
        # Example of default values is default_values = {'Datasets' : ['RNET', 'DNET'] , 'Model': ['MODEL_PATH'],
        # 'RESULT' : ['FOLDER_PATH', 'DATASET_TRAIN_CSV', 'DATASET_TEST_CSV', 'PREVIOUSLY_VALIDATED_CSV']
        self._section_names = self.default_values_in_sections.keys()
        self._default_string_value = 'None'

        if not os.path.isfile(self.config_file) or self.get_new_config:
            self.create_config()

    def create_config(self):
        """
        Function to create the config file using the provided default keys
        """
        dataset_config = configparser.ConfigParser()
        for section in self._section_names:
            dataset_config.add_section(section)
            _section_keys = self.default_values_in_sections[section]
            for _section_key in _section_keys:
                _new_value = self._read_config_and_update(section_name=section, key=_section_key)
                dataset_config.set(section, _section_key, _new_value)

        with open(self.config_file, 'w') as _config_file:
            dataset_config.write(_config_file)

    def _read_config_and_update(self, section_name, key):
        """
        Function to update the values in the config file.
        It reads the file and prompts the user about the previous value and
        lets the user to keep the previous value (if present)
        :param section_name: name of the section, in which value is needed to be updated
        :param key: name of the section key, whose value is to written or updated
        :return: value to be placed in the corresponding key in the required section
        """
        if os.path.isfile(self.config_file):
            try:
                dataset_config = configparser.ConfigParser()
                dataset_config.read(self.config_file)
                previous_value = dataset_config[section_name][key]
            except KeyError:
                previous_value = self._default_string_value
        else:
            previous_value = self._default_string_value

        if previous_value == self._default_string_value:
            _query_string = 'Path for {0}. Enter new value : '.format(
                key, previous_value)
        else:
            _query_string = 'Path for {0}. Previous value = {1}. Press y to use previous value or enter new value : '.format(
                key, previous_value)

        _input = input(_query_string)
        if _input == 'y' or _input == 'Y' or _input == '\r':
            return previous_value
        else:
            return _input

    def _read_config_from_ini_file(self, config_object, section_name, key):
        """
        Function to read a specific value from the ini file.
        :param config_object: python's config parser object to used for reading the ini file
        :param section_name: name of the section, from which values are to be read
        :param key: key of the required section, whose value would be read
        :return: value from the config file
        """
        try:
            return config_object[section_name][key]
        except KeyError:
            return self._default_string_value

    def read_config(self):
        """
        Function to read all values from the ini file
        :return: two-tiered dictionary, with section names as first level keys and value keys as second level keys.
        """
        dataset_config = configparser.ConfigParser()
        dataset_config.read(self.config_file)
        _config = dict()

        for section_name in self._section_names:
            _section_dict = dict()
            for section_key in self.default_values_in_sections[section_name]:
                _section_dict[section_key] = self._read_config_from_ini_file(config_object=dataset_config,
                                                                             section_name=section_name,
                                                                             key=section_key)
            _config[section_name] = _section_dict

        return _config
