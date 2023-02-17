#!/usr/bin/env bash
set -e

. ~/.virtualenvs/python3/bin/activate

PYTHONPATH=. python3 test.py

echo "hello, today is $(date)"
