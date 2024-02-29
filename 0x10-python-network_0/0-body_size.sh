#!/bin/bash
# This script takes a URL as input, sends a request to that URL using curl.

curl -sI $1 | grep "Content-Length" | cut -d " " -f2
