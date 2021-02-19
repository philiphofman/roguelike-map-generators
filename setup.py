from setuptools import setup, find_packages

setup(
    name="rmg",
    packages=find_packages(where='rmg'),
    package_dir={'': 'rmg'},
)
