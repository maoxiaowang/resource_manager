"""
生成默认env
"""
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from jinja2 import Template

BASE_DIR = Path(__file__).resolve().parent


class EnvGenerator(object):
    template_path = '.env.template'
    env_path = '.env'

    def __init__(self):
        if (BASE_DIR / '.env').exists():
            print('The ".env" file already exists.')
            exit(1)

    @property
    def context(self):
        return {
            'django_debug': 1,
            'django_secret_key': get_random_secret_key(),
            'django_allowed_hosts': '*',
            'django_trusted_origins': 'http://localhost:3000'
        }

    def render(self):
        with open(self.template_path, 'r') as template_file:
            template_content = template_file.read()

        template = Template(template_content)
        return template.render(self.context)

    def generate(self):
        with open(self.env_path, 'w') as env_file:
            env_file.write(self.render())


if __name__ == '__main__':
    EnvGenerator().generate()
