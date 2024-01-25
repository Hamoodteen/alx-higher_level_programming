#!/bin/bash
#commentttttttttttttttttttttttttttttt
curl -X OPTIONS --head -s -i "$1" | grep -i allow | sed '1d; s/Allow: //i'
