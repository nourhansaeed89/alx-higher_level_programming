#!/bin/bash
# Check if the user provided a URL as an argument
curl -sX GET $1 -L
