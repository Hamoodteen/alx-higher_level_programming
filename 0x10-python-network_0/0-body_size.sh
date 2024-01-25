#!/bin/bash
#commentttttttttttttttttttttttttttttt
curl -s -o /dev/null -w "%{size_download}\n" $1
