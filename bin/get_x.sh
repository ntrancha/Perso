#!/bin/sh

xdotool getmouselocation | awk '{print $1}' | sed -e "s/x://g"
