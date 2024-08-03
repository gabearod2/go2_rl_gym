from setuptools import find_packages
from distutils.core import setup

setup(name='go2_rl_gym',
      version='1.0.0',
      author='Gabriel Rodriguez',
      license="BSD-3-Clause",
      packages=find_packages(),
      author_email='gabearod2@gmail.com',
      description='RL environment for training the Go2',
      install_requires=['isaacgym', 'rsl-rl', 'matplotlib', 'numpy==1.20', 'tensorboard'])
