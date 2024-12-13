#!/bin/sh
agentql init
export
AGENTQL_API_KEY=xJ2gYetiuPm2qbQl_h5ietTOPGaO38BsEUyuGcWDGaoNEcGhoBMMZA
pytest -v -s test_bookies.py
#echo "Starting HTTP server on port 8000 to serve the screenshot..."
#python3 -m http.server 8000 --directory /output to
