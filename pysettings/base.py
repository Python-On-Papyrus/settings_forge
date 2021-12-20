from pysettings.exceptions import SettingsException


class BaseSettings:
    _settings: dict = {}

    def read_input_file(self, filename):
        raise NotImplementedError()

    def parse_input_file(self, file):
        raise NotImplementedError()

    def __init__(self, filename: str = None):
        try:
            settings_data = self.parse_input_file(self.read_input_file(filename=filename))

            for setting_key, setting_value in settings_data.items():
                self._settings[setting_key] = setting_value

        except Exception as exc:
            raise SettingsException(exc) from exc

    def __getattr__(self, item):
        return self._settings[item]

    def dumps(self) -> str:
        raise NotImplementedError()

    def __str__(self):
        return self.dumps()
