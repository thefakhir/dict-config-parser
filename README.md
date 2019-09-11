### ConfigParser
A custom wrapper, written for python's own configparser, for reading and writing ini files, using simple dictionaries.

Can be installed using the setup.py file and by using the pip module

    pip install dict-config-parser

##### Input arguments:


* config_file

As the name suggest, you can input the file name of the file, including the ini extension. 
You can also pass the path of the config file in this parameter.
  
  * get_new_config
  This is a boolean flag, when True, the code would ask for a new config and overwrite the previous one.
  
  * default_keys
  
  A dictionary needs to be passed to this input parameter. The keys of the dictionary would become the section names of the config file, while the array of values, against those keys, would become the section keys in that particular section. (See the test case for understanding)
  
  A sample default keys might look this.
  
    keys = {'DATASET_PATH' : ['VOC' , 'COCO'],
            'MODEL_PATH'   : ['WEIGHTS', 'JSON']}'

                        
##### Usage:

You only have to pass through the input parameters and it would create a new file, if it doesn't already exist. 
This would create the required prompts on the command line and you can enter the values as needed.

    config = ConfigParser(config_file='config.ini', get_new_config=True, default_keys=keys)


After creating the file, you would need to run the run_config method, from the current object of the class, to read the values 
from the created config file and return the values in a two-tiered dictionary.

    config_dictionary = config.read_config()

The dictionary would have sections names, as its first tier keys and section key, as its second tier keys.
 
For example, if you passed the example default keys, you could get the value against 'JSON' key in the 'MODEL_PATH' section,
by the command 
 
    required_value = config_dictionary['MODEL_PATH']['JSON']
