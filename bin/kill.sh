#!/bin/sh

pid=`cat ../tmp/pid.txt`
kill -9 $pid
