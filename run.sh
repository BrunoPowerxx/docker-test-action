#!/bin/sh
agentql init
export AGENTQL_API_KEY=AtqNf3kHb3TAbMjU08U0x4zVZGLbVej72uol03Irg_AqFOW3642GOw
pytest -v -s test_bot.py
#python3 -m http.server 8000 --directory /output to
