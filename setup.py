import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='azure-storage-python',
    version='0.0.1',
    author='Andrei Papou',
    author_email='andrei.papou@itechart-group.com',
    description='Async Python client for Azure SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/andrei-papou/azure-storage-python',
    packages=setuptools.find_packages(),
    install_requires=[
        'aiodns==1.1.1',
        'aiohttp==3.0.9',
        'asn1crypto==0.24.0',
        'async-timeout==2.0.1',
        'attrs==17.4.0',
        'azure-common==1.1.8',
        'azure-nspkg==2.0.0',
        'cchardet==2.1.1',
        'cffi==1.11.5',
        'chardet==3.0.4',
        'cryptography==2.1.4',
        'idna==2.6',
        'idna-ssl==1.1.0',
        'multidict==4.1.0',
        'pycares==2.3.0',
        'pycparser==2.18',
        'python-dateutil==2.7.0',
        'PyYAML==3.12',
        'six==1.11.0',
        'urllib3==1.22',
        'vcrpy==1.11.1',
        'wrapt==1.10.11',
        'yarl==1.1.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
    ]
)
