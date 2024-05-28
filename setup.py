#!/usr/bin/env python
from setuptools import dist

dist.Distribution().fetch_build_eggs(['setuptools_rust'])
from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="python-extensions.rs",
    version="0.1",
    rust_extensions=[RustExtension(
        ".python_extensions_rs.python_extensions_rs",
        path="Cargo.toml", binding=Binding.PyO3)],
    packages=["python_extensions_rs"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
    ],
    zip_safe=False,
)
