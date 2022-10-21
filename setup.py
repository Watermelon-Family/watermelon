# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(name='watermelon-todo-list',
      version='0.0.1',
      description='watermelon, inspired by tomato impl by python',
      author="ruanjiancheng",
      author_email="1434919953@qq.com",
      url='https://github.com/Watermelon-Family/watermelon',
      packages=find_packages(),
      long_description="watermelon",
      long_description_content_type='text/markdown',
      classifiers=[
          'Programming Language :: Python :: 3',
          'Operating System :: OS Independent'
      ],
      python_requires='>=3.7',
      entry_points={"console_scripts": ["watermelon = watermelon.__main__:main"]},
      include_package_data=True,
      install_requires=[
          'python-dateutil>=2.7.0,<5.0.0',
          'prettytable>= 3.2.0,<5.0.0'
      ])