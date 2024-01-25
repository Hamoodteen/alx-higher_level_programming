#!/bin/bash
#commentttttttttttttttttttttttttttttt
$res = $(curl -w "%{http_code}" -s -o /dev/null $1)
if [ "$res" == 200 ]; then
    curl -s $1
fi
