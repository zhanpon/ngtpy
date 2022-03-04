import sys

try:
    from skbuild import setup
except ImportError:
    print(
        "Please update pip, you need pip 10 or greater,\n"
        " or you need to install the PEP 518 requirements in pyproject.toml yourself",
        file=sys.stderr,
    )
    raise

from setuptools import find_packages

setup(
    name="ngtpy",
    version="0.2.b0",
    description="ngt python",
    author="Yahoo! JAPAN research",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    cmake_install_dir="src/ngtpy",
    include_package_data=True,
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
    install_requires=["numpy"],
)
