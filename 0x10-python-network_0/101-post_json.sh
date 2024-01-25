#!/bin/bash
#commentttttttttttttttttttttttttttttt
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
