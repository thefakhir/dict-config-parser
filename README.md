### ConfigParser
A custom wrapper for , written for python's own configparser, for reading and writing ini files, using simple dictionaries.

##### Input arguments:


* config_file

As the name suggest, you can input the file name
 of the file, including the ini extension. 
 You can also pass the path of the config file in this
  parameter.
  
  * get_new_config
  
  This is a boolean flag, when True, the code would ask for a new config and overwrite the previous one.
  
  * default_keys
  
  A dictionary needs to be passed to this input parameter. The keys of the dictionary would become the section names of the config file, while the array of values, against those keys, would become the section keys in that particular section. (See the test case for understanding)
  
  A sample default keys might look this.
  
    default_keys = {'DATASET_PATH' : ['VOC' , 'COCO'],
                    'MODEL_PATH'   : ['WEIGHTS', 'JSON']}'

##### Usage:

After passing the required input parameters, you would need to run create_config method from the object created. 
This would create the required prompts on the command line and you can enter the values as needed.

    config = ConfigParser(input_parameters)'
    config.create_config()


After creating the file, you would need to run the run_config method, from the current object of the class, to read the values 
from the created config file and return the values in a two-tiered dictionary.

    config_dictionary = config.read_config()

The dictionary would have sections names, as its first tier keys and section key, as its second tier keys.
 
For example, if you passed the example default keys, you could get the value against 'JSON' key in the 'MODEL_PATH' section,
by the command 
 
    required_value = config_dictionary['MODEL_PATH']['JSON']


TODO:

- [] Add support to change subset of values  