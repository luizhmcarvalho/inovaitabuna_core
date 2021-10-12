from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in inovaitabuna_core/__init__.py
from inovaitabuna_core import __version__ as version

setup(
	name="inovaitabuna_core",
	version=version,
	description="InovaItabuna",
	author="Giovani",
	author_email="itabuna@itabuna.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
