from setuptools import setup, find_packages
import os

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
]

dist = setup(
    name='cf_core',
    version='0.1',
    author='Darko Aleksovski',
    description='Package providing core utilities and widgets for ClowdFlows 2.0',
    url='https://github.com/xflows/cf_core',
    license='MIT License',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
