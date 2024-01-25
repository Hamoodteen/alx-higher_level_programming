#!/bin/bash
#commentttttttttttttttttttttttttttttt
if [[ $(curl -w "%{http_code}" -s -o /dev/null $1) == "200" ]]; then curl -s $1; fi
