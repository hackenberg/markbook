from setuptools import setup, find_packages

setup(
    name="markbook",
    version="0.0.1",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["flask", "flask_sqlalchemy", "markdown"],
    entry_points={
        "console_scripts": [
            "markbook = markbook:cmdline.main",
        ],
    },
    test_suite="tests",
    license="MIT",
)
