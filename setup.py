from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rodtep_claim_management/__init__.py
from rodtep_claim_management import __version__ as version

setup(
	name="rodtep_claim_management",
	version=version,
	description="Rodtep Claim Management",
	author="FinByz",
	author_email="info@finbyz.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
