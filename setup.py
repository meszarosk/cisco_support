import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="cisco_support_API",
    version="0.0.1",
    author="Karoly Meszaros",
    author_email="meszaros.karoly@bitmen.hu",
    description="Python implementation of the Cisco Support APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meszarosk/cisco_support",
    project_urls={
        "Bug Tracker": "https://github.com/meszarosk/cisco_support/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.11",
)