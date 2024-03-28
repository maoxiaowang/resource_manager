"""
生成或更新默认env文件
"""
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from dotenv import dotenv_values
from jinja2 import Template

BASE_DIR = Path(__file__).resolve().parent

DEFAULT_ENVS = {
    'django_debug': 1,
    'django_secret_key': get_random_secret_key(),
    'django_allowed_hosts': '*',
    'django_trusted_origins': 'http://localhost:3000',

    'database_name': 'resource',
    'database_user': 'postgres',
    'database_password': '',
    'database_host': 'localhost',
    'database_port': 5432
}


class EnvGenerator(object):
    template_path = '.env.template'
    env_path = '.env'

    def __init__(self):
        self.env_path = BASE_DIR / self.env_path
        self.template_path = BASE_DIR / self.template_path

    def render(self, values):
        with open(self.template_path, 'r') as template_file:
            template_content = template_file.read()

        template = Template(template_content)
        return template.render(values)

    def generate(self):
        if self.env_path.exists():
            action = 'updated'
            exist_envs = dotenv_values(self.env_path)
            envs = dict()
            for key, value in DEFAULT_ENVS.items():
                envs[key] = exist_envs[key] if key in exist_envs else value
        else:
            action = 'created'
            envs = DEFAULT_ENVS
        with open(self.env_path, 'w') as env_file:
            env_file.write(self.render(envs))
        print(f'The ".env" file has been {action}.')


if __name__ == '__main__':
    EnvGenerator().generate()
