from setuptools import setup

__version__ = 'unknown'
with open('tracking_url/version.py') as version_file:
    exec(version_file.read())

with open('README.rst') as readme_file:
    long_description = readme_file.read()

setup(
    name='tracking-url',
    packages=[
        'tracking_url',
        'tracking_url.tests'],
    version=__version__,
    description='Detect package carrier from tracking number and generate tracking url',
    long_description=long_description,
    author='Kevin Michel',
    author_email='kevin.michel@sereema.com',
    url='https://github.com/sereema/tracking-url',
    download_url='https://github.com/sereema/tracking-url/archive/v{}.tar.gz'.format(__version__),
    keywords=['tracking', 'number', 'package', 'carrier', 'url', 'ups', 'fedex', 'usps', 'dhl'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])
