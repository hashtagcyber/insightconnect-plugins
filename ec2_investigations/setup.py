# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="ec2_investigations-rapid7-plugin",
      version="1.0.1",
      description="EC2 Investigations runs security tools on the AWS EC2 platform. Using the EC2 Investigations plugin for Rapid7 InsightConnect will allow users to mount drives and scan directories with ClamAV",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_ec2_investigations']
      )
