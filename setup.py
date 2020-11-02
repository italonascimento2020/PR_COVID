from setuptools import setup, find_packages

requires = [
    "click==7.1.2",
    "pandas==1.0.5",
    "requests==2.24.0",
    "numpy==1.19.0"
]

setup(
    name="app",
    packages=find_packages(),
    install_requires=requires,
)