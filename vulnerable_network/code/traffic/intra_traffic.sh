#!/bin/bash

while true; do
	sleep $(($RANDOM / 1000))
	wget --force-html -r -l2 --spider  http://182.170.2.2:8080/ 2>/dev/null
done
