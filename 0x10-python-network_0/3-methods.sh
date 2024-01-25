#!/bin/bash
#commentttttttttttttttttttttttttttttt
curl -s "$1" | grep "Allow" | cut -d " " -f2-
