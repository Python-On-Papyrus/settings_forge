try:
    import yaml
except ImportError:
    pass

from pysettings.base import BaseSettings


class YamlSettings(BaseSettings):
    def read_input_file(self, filename):
        return open(filename, 'r', encoding='utf-8')

    def parse_input_file(self, file):
        return yaml.safe_load(file)

    def dumps(self) -> str:
        return yaml.dump(self._settings)
