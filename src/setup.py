import setuptools
from app import __version__


setuptools.setup(
    name='techs_draft',
    version=__version__,
    description='A fastapi based microservice',
    long_description='',
    author='Kevin Kalis',
    url='',
    download_url='https://github.com/LowerSilesians/techs.draft',
    license='All rights reserved',
    namespace_packages=[],
    package_dir={'': '.'},
    packages=[],
    include_package_data=True,
    install_requires=[
    ],
    entry_points='''
        [console_scripts]
    '''
)
