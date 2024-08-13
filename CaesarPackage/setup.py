from setuptools import setup

with open("requirements.txt") as rq:
    requirements = rq.read().split('\n')

setup(
    name='CaesarPackage',
    version='0.0.1',
    author='Abeer_Omar',
    packages=['CaesarPackage'],
    # license='LICENSE.txt',
    description='Package that encrypts data using Caesar Cipher',
    # long_description=open('README.txt').read(),
    install_requires=[requirements],
)
