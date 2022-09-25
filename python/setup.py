from os.path import exists
from setuptools import setup

setup(
    name='{{ repo_name }}',
    version='0.1.0',
    url="https://github.com/{{ github_username }}/{{ repo_name}}",
    license="MIT",
    description="My new package.",
    long_description=open("README.md").read() if exists("README.md") else "",
    long_description_content_type='text/markdown',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
)
