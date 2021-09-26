from setuptools import find_packages
from setuptools import setup

from volcengine import VERSION

setup(
    name="volcengine",
    version=VERSION,
    keywords=("pip", "volcengine", "volc-sdk-python"),
    description="The Volcengine SDK for Python",
    license="MIT Licence",
    url="https://github.com/Volcengine/volc-sdk-python",
    author="Volcengine SDK",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["requests", "pytz", "pycryptodome", "protobuf", "google", "six"],
)
