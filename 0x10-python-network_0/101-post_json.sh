#!/bin/bash
#commentttttttttttttttttttttttttttttt
curl -s $1/$2 | jq '.' >/dev/null 2>&1 && echo "Valid JSON" || echo "Not a valid JSON"
