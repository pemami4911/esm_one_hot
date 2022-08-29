# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup


with open("esm_one_hot/version.py") as infile:
    exec(infile.read())

with open("README.md") as f:
    readme = f.read()


setup(
    name="fair-esm-one-hot",
    version=version,
    description="Evolutionary Scale Modeling (esm): Pretrained language models for proteins. From Facebook AI Research. Modified by Patrick Emami.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Patrick Emami",
    url="https://github.nrel.gov/pemami/esm",
    license="MIT",
    packages=["esm_one_hot"],
    data_files=[("source_docs/esm_one_hot", ["LICENSE", "README.md", "CODE_OF_CONDUCT.rst"])],
    zip_safe=True,
)
