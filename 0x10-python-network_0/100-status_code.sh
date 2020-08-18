#!/bin/bash
# Sends argument to url
curl -sL -w "%{http_code}" -I "$1" -o /dev/null
