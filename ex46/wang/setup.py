try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
	'description': 'An example.',
	'author': 'Snowball Wang',
	'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
	'author_email': 'guy@guy.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['wang'],
	'scripts': [],
	'name': 'wang'
}

setup(**config)
