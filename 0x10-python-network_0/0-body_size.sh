#!/bin/bash
# This script takes a URL as input, sends a request to that URL using curl.

# Send a GET request to the URL and save the response body to a temporary file
curl -s "$1" > temp_body.txt

# Get the size of the body of the response in bytes and display it
wc -c < temp_body.txt

# Remove the temporary file
rm temp_body.txt
