from setuptools import setup
import sys


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='system-manager',
      version='0.1.0',
      description="Cross-platform unix-like systems administration wrapper",
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
        "Intended Audience :: Developers",
        ],
      url='https://github.com/heywoodlh/system-manager',
      author='Spencer Heywood',
      author_email='l.spencer.heywood@protonmail.com',
      license='APACHE-2.0',
      packages=['system-manager'],
      scripts=['bin/system-manager'],
      python_requires='>3.5.2',
      install_requires=[
          'distro'
      ],
      zip_safe=False)
