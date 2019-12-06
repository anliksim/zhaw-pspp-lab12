from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_file = f.read()

setup(
    name='zhaw-pspp-lab12',
    version='1.0.0',
    description='PSPP lab usig python',
    long_description=readme,
    author='Simon Anliker',
    author_email='anliksim@students.zhaw.ch',
    url='https://github.com/anliksim/zhaw-pspp-lab12',
    license=license_file,
    packages=find_packages(exclude='tests')
)
