#! /bin/bash


PYTHONPATH="${PYTHONPATH}:`pwd`" pytest -s tests/ "$@"
