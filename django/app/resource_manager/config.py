from common.envs import EnvSection

__all__ = [
    'env'
]


class EnvManager(object):
    django = EnvSection('django')
    database = EnvSection('database')

env = EnvManager()
