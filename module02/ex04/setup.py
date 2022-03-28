from setuptools import setup

with open("README.md", 'r') as readme:
    long_description = readme.read()

setup(
    name='my_minipack',
    version='1.0.0',
    description='this package contains some simple functions.',
    homepage='None',
    author='aihya',
    author_email='aihya@student.1337.ma',
    license='GPLv3',
    py_modules=['progressbar', 'logger'],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type='text/markdown',
    installer='pip',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education",
        "Topic :: Package",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only"
    ]
)