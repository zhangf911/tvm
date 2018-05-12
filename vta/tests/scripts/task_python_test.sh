#!/bin/bash

export PYTHONPATH=python:nnvm/python:nnvm/tvm/python:nnvm/tvm/topi/python

echo "Running unittest..."
python -m nose -v tests/python/unittest || exit -1
python3 -m nose -v tests/python/unittest || exit -1

echo "Running integration test..."
python -m nose -v tests/python/integration || exit -1
python3 -m nose -v tests/python/integration || exit -1