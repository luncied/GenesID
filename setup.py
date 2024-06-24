from setuptools import find_packages, setup

setup(
    name="GetAPIResults",
    version="1.0",
    description="",
    author="",
    author_email="",
    packages=find_packages(where="src"),  # same as name
    install_requires=[
        "setup",
        "python_dotenv",
        "os",
    ],  # external packages as dependencies
    scripts=[
        "scripts/cool",
        "scripts/skype",
    ],
)
