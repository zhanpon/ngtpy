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
    version="0.1.1",
    description="ngt python",
    author="Yahoo! JAPAN research",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    cmake_install_dir="src/ngtpy",
    #cmake_args=["-DNGT_MARCH_NATIVE_DISABLED=ON", "-DNGT_AVX_DISABLED=ON"],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
    install_requires=["numpy"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: Apache Software License",
    ],
)
