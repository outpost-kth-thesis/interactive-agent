#!/bin/bash
mitmdump -p 8080 -q -s scripts/flow.py & sleep 2


xvfb-run python src/main.py