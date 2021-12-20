import json

from pysettings.base import BaseSettings


class JsonSettings(BaseSettings):
    def read_input_file(self, filename):
        return open(filename, 'r', encoding='utf-8')

    def parse_input_file(self, file):
        return json.load(file)

    def dumps(self) -> str:
        return json.dumps(self._settings, indent=2)
