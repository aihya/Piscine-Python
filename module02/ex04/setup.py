from setuptools import setup, find_namespace_packages

with open("README.md", 'r') as readme:
    long_description = readme.read()

setup(
    name='my_minipack',
    version='1.0.0',
    description='this package contains some simple functions.',
    author='aihya',
    author_email='aihya@student.1337.ma',
    url='None',
    license='GPLv3',
    py_modules=['my_minipack/progressbar', 'my_minipack/logger'],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)