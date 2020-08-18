#!/bin/bash
# sends POST request
curl "$1" -sX POST -H "Content-Type: application/json" -d @"$2" 
