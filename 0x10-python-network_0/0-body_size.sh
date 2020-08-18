#!/usr/bin/env bash
# Display the length of the response
curl -sI "$1" | awk -v FS=": " '/^Content-Length/{print $2}'
