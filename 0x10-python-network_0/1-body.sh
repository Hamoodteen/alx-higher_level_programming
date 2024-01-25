#!/bin/bash
#commentttttttttttttttttttttttttttttt
curl -s -o /dev/null -w "%{http_code}" "$1" | tail -n +2 && curl -s "$1"
