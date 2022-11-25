from setuptools import setup

setup(
    name="trentubuddy",
    version="0.1.0",
    packages=["src"],
    entry_points={
        "console_scripts": [
            "trentubuddy = src.__main__:main"
        ]
    },
)
