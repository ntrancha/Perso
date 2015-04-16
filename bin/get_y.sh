#!/bin/sh

xdotool getmouselocation | awk '{print $2}' | sed -e "s/y://g"
