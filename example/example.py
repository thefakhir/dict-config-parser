# Author Fakhir Khan

from dict_config_parser import ConfigParser


def test():
    default_values = {'Datasets': ['VOC', 'COCO'],
                      'Model': ['MODEL_PATH'],
                      'RESULT': ['RESULT_FOLDER_PATH', 'DATASET_TRAIN_CSV', 'DATASET_TEST_CSV']}
    input_params = {'config_file': 'config.ini',
                    'get_new_config': True,
                    'default_keys': default_values}
    config = ConfigParser(input_parameters=input_params)
    config.create_config()
    config_after_reading = config.read_config()
    print(config_after_reading)


if __name__ == '__main__':
    test()
