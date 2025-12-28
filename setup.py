from setuptools import setup, find_packages

setup(
    name="curr_conv",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytest",
        "flake8",
    ],
    entry_points={
        "console_scripts": [
            "curr-conv=curr_conv.cli.main:main",
        ],
    },
)