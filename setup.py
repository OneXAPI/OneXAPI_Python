from setuptools import setup, find_packages
from os import path

readme = path.join(path.abspath(path.dirname(__file__)), 'README.md')
with open(readme, encoding='utf-8') as f:
    long_description = f.read()

project_urls = {
    'Homepage': 'https://github.com/OneXAPI/OneXAPI_Python',
    'Documentation': 'https://onexapi.github.io/OneXAPI-Reference/'
}

setup(
    name='OneXAPI',
    version='0.0.2',
    description='For Beta Test',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Libera Inc.',
    author_email='ceo@libera.or.kr',
    url=project_urls['Homepage'],
    project_urls=project_urls,
    packages=['OneXAPI',
              'OneXAPI.Upbit',
              'OneXAPI.Binance',
              'OneXAPI.internal',
              'OneXAPI.internal.instruments'
              ],  # would be the same as name
    include_package_data=True,
    install_requires=['tqdm==4.64.1'], #external packages acting as dependencies
    scripts=[],
    python_requires='>=3.6',
)