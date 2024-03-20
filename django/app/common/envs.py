import os


class EnvNotFoundError(Exception):

    def __init__(self, key):
        self.key = key

    def __str__(self):
        return f'The environment variable {self.key} was not found.'


class EnvWrongTypeError(Exception):

    def __init__(self, key, _type: str):
        self.type = _type
        self.key = key

    def __str__(self):
        return f'The environment variable {self.key} is not type of {self.type}.'


class EnvSection(object):

    def __init__(self, prefix):
        self._prefix = prefix.upper()
        if self._prefix and not self._prefix.endswith('_'):
            self._prefix += '_'

    def _full_key(self, key):
        return f'{self._prefix}{key.upper()}'

    def get(self, key: str, default=None, allow_null=False):
        full_key = self._full_key(key)
        value = os.environ.get(full_key, default)
        if value is None and not allow_null:
            raise EnvNotFoundError(full_key)
        return value

    def get_int(self, key, default=None):
        if default is not None:
            assert isinstance(default, int)
        try:
            value = self.get(key)
        except EnvNotFoundError:
            if default is not None:
                return default
            raise
        try:
            return int(value)
        except TypeError:
            raise EnvWrongTypeError(self._full_key(key), 'int')

    def get_float(self, key, default=None):
        if default is not None:
            assert isinstance(default, float)
        try:
            value = self.get(key)
        except EnvNotFoundError:
            if default is not None:
                return default
            raise
        try:
            return float(value)
        except TypeError:
            raise EnvWrongTypeError(self._full_key(key), 'float')

    def get_bool(self, key, default: bool = None):
        if default is not None:
            assert isinstance(default, bool)
        try:
            value = bool(self.get_int(key))
        except EnvNotFoundError:
            if default is not None:
                return default
            raise
        except TypeError:
            raise EnvWrongTypeError(self._full_key(key), 'bool')
        return value

    def get_list(self, key, default: list = None, separator=' '):
        try:
            value = self.get(key)
        except EnvNotFoundError:
            if default is not None:
                return default
            raise
        return value.split(separator)
