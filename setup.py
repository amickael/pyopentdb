from setuptools import setup, find_packages

import pyopentdb

with open("README.md", "r") as f:
    readme = f.read()

with open("requirements.txt", "r") as f:
    requirements = [i.rstrip() for i in f.readlines()]

setup(
    name="pyopentdb",
    version=pyopentdb.__version__,
    description=pyopentdb.__description__,
    long_description=readme,
    long_description_content_type="text/markdown",
    author=pyopentdb.__author__,
    author_email="andrew.mickael@gmail.com",
    license="MIT",
    platforms=["NT", "POSIX"],
    url="https://github.com/amickael/pyopentdb",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.6",
)
