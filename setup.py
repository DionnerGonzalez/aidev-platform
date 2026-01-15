from setuptools import setup, find_packages

setup(
    name="aidev_platform",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask"
    ],
    entry_points={
        "console_scripts": [
            "aidev=aidev_platform.cli.cli_main:main"
        ]
    },
)
