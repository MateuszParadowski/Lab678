#!/usr/bin/python
import yaml

dict_sample = {'info': {'description': 'text', 'list_example': ['one', 'two'], 'test_name': 'yaml_test', 'timeout': 100}, 'name': 'Config'}

x = yaml.dump(dict_sample)
print(x)
