import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    user_options = [("pytest-args=", "a", "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name="markbook",
    version="0.0.1",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "markbook = markbook.manage:main",
        ],
    },
    cmdclass={"test": PyTest},
    install_requires=[
        "flask", "flask_migrate", "flask_script", "flask_sqlalchemy",
        "markdown",
    ],
    tests_require=["pytest"],
    license="MIT",
    zip_safe=False,
)
