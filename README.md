# Settings forge - the future of configurations

Settings forge is the module that helps you to serialize your configuration files into Python objects.

------------------------------------

### Installation
`pip install settings-forge`
###### If you want to use YAML configuration files, then you are required to install [pyyaml](https://github.com/yaml/pyyaml).

------------------------------------

### Usage
- Create a file with the settings. We will use JSON as the example(`settings.json`):
````json
{
    "username": "PythonOnPapyrus",
    "database": {
        "host": "db_host",
        "port": 12345,
        "password": "mypassword",
        "additional": {
            "ssl": true,
            "sessions": 100
        }
    },
    "uses_passwords": true,
    "version": 1
}
````
- Create a python file where your will create your settings(`settings.py`):
````python
from settings_forge import JsonSettings

settings = JsonSettings("settings.json")
print(settings)
````
- Now, you can use your settings as a normal Python object:
````python
USERNAME = settings.username
DATABASE_HOST = settings.database['host']
````

------------------------------------

### Available languages
- JSON
- YAML(you need to install pyyaml)


------------------------------------

### If you want to add your own languages
All you need to do is import `settings_forge.BaseSettings` and
reassign those functions:
- `read_input_file()` - open the input file and return it
- `parse_input_file()` - parse the file data
- `dumps()` - serialize all the settings to a string
