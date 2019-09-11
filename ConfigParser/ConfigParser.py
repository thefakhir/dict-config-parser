#  Author Fakhir Khan

import configparser
import os


class ConfigParser:
    def __init__(self, input_parameters):
        if 'config_file' in input_parameters:
            self.config_file = input_parameters['config_file']
        else:
            self.config_file = 'config.ini'

        if 'get_new_config' in input_parameters:
            self.get_new_config = input_parameters['get_new_config']
        else:
            self.get_new_config = False

        assert 'default_keys' in input_parameters, 'Values were not given'
        # This should be a dictionary of dictionaries where first level keys should be the section names and second
        # level keys should be the default keys of the respective section
        self.default_values_in_sections = input_parameters['default_values']
        # Example of default values is default_values = {'Datasets' : ['RNET', 'DNET'] , 'Model': ['MODEL_PATH'],
        # 'RESULT' : ['FOLDER_PATH', 'DATASET_TRAIN_CSV', 'DATASET_TEST_CSV', 'PREVIOUSLY_VALIDATED_CSV']
        self.section_names = self.default_values_in_sections.keys()

        self.default_string_value = 'None'

    def create_config(self):

        dataset_config = configparser.ConfigParser()
        for section in self.section_names:
            dataset_config.add_section(section)
            _section_keys = self.default_values_in_sections[section]
            for _section_key in _section_keys:
                _new_value = self.__read_config_and_update(section_name=section, key=_section_key)
                dataset_config.set(section, _section_key, _new_value)

        with open(self.config_file, 'w') as _config_file:
            dataset_config.write(_config_file)

    def __read_config_and_update(self, section_name, key):
        if os.path.isfile(self.config_file):
            try:
                dataset_config = configparser.ConfigParser()
                dataset_config.read(self.config_file)
                previous_value = dataset_config[section_name][key]
            except KeyError:
                previous_value = self.default_string_value
        else:
            previous_value = self.default_string_value

        if previous_value == self.default_string_value:
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

    def __read_config_from_ini_file(self, config_file, section_name, key):
        try:
            return config_file[section_name][key]
        except KeyError:
            return self.default_string_value

    def read_config(self):
        dataset_config = configparser.ConfigParser()
        dataset_config.read(self.config_file)
        _config = dict()

        for section_name in self.section_names:
            _section_dict = dict()
            for section_key in self.default_values_in_sections[section_name]:
                _section_dict[section_key] = self.__read_config_from_ini_file(config_file=dataset_config,
                                                                              section_name=section_name,
                                                                              key=section_key)
            _config[section_name] = _section_dict

        return _config

