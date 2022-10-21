from setuptools import setup, find_packages

setup(
    name='OneXAPI',
    version='0.0.1',
    description='For Beta Test',
    author='Libera Inc.',
    author_email='ceo@libera.com',
    url='https://github.com/OneXAPI',
    packages=['OneXAPI',
              'OneXAPI.Upbit',
              'OneXAPI.Upbit.Indonesia',
              'OneXAPI.Upbit.Singapore',
              'OneXAPI.Upbit.Thailand',
              'OneXAPI.Binance',
              'OneXAPI.internal',
              'OneXAPI.internal.instruments'
              ],  # would be the same as name
    include_package_data=True,
    install_requires=['tqdm==4.64.1'], #external packages acting as dependencies
    scripts=[],
    python_requires='>=3.6',
)