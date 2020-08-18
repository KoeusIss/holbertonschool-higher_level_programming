#!/bin/bash
# displays available http method
curl -sI "$1" | awk -v FS=": " '/^Allow/{print $2}'
