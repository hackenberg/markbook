from setuptools import setup, find_packages

setup(
    name="markbook",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["flask", "markdown"],
    entry_points={
        "console_scripts": [
            "markbook = main:main",
        ],
    },
    license="MIT",
)
