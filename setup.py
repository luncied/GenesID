from setuptools import setup

setup(
  name='GetAPIResults',
  version='1.0',
  description='',
  author='',
  author_email='',
  packages=[''],  #same as name
  install_requires=['setup', 'dotenv', 'os'], #external packages as dependencies
  scripts=[
            'scripts/cool',
            'scripts/skype',
          ]
)