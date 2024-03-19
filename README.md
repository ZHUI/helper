# tool_helpers
Package for helpers.cpp 

> https://github.com/PaddlePaddle/PaddleNLP/blob/develop/model_zoo/ernie-1.0/data_tools/helpers.cpp

Build linux packages.
```
docker run --rm -e PLAT=manylinux2014_x86_64 -v `pwd`:/io quay.io/pypa/manylinux2014_x86_64 bash -x /io/package/build.sh
# upload wheel
python -m twine upload ./wheelhouse/* --verbose
```

build for local useage.
```
pip wheel ./ --no-deps -w wheelhouse/
```
