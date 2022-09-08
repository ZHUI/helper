# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import re
import sys
import setuptools
from pybind11.setup_helpers import Pybind11Extension

workdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(workdir, './requirements.txt')) as f:
    requirements = f.read().splitlines()

cur_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(cur_dir, 'README.md'), 'rb') as f:
    lines = [x.decode('utf-8') for x in f.readlines()]
    lines = ''.join([re.sub('^<.*>\n$', '', x) for x in lines])
    LONG_DESC = lines

compile_extra_args = [
    "-O3", "-Wall", "-shared", "-std=c++11", "-fPIC", "-fdiagnostics-color"
]
link_extra_args = []

if sys.platform == "darwin":
    compile_extra_args = ["-mmacosx-version-min=10.9"]
    link_extra_args = ["-stdlib=libc++", "-mmacosx-version-min=10.9"]

extensions = [
    Pybind11Extension(
        "tool_helpers.helpers",
        sources=[os.path.join("helpers.cpp")],
        # include_dirs=[],
        language="c++",
        extra_compile_args=compile_extra_args,
        extra_link_args=link_extra_args,
    ),
]

setuptools.setup(
    name="tool_helpers",
    version="0.1.1",
    author="PaddleNLP Team",
    author_email="paddlenlp@baidu.com",
    description="Data tool helpers for PaddleNLP pre-training.",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    url=
    "https://github.com/PaddlePaddle/PaddleNLP/blob/develop/model_zoo/ernie-1.0/data_tools",
    packages=setuptools.find_packages(where='.', exclude=('tests*')),
    setup_requires=['cython', 'numpy', 'pybind11'],
    install_requires=requirements,
    ext_modules=extensions,
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: C++',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    license='Apache 2.0')
