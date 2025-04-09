# setup.py
from setuptools import setup, find_packages

setup(
    name="soperator",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["openai", "python-dotenv"],
    entry_points={
        "console_scripts": [
            "soperator=soperator.main:main"
        ]
    },
)
