#! /bin/bash


PYTHONPATH="${PYTHONPATH}:`pwd`" pytest -s tests/ "$@" --log-cli-level=DEBUG
