#!/bin/sh
agentql init
export AGENTQL_API_KEY=3xOoDfRXU-Wuc1eQeSqhjclCk-E9kb-nP4gAJEUfeOmZOJUhd0IEwg
pytest -v -s test_bot.py
#python3 -m http.server 8000 --directory /output to
