#!/bin/sh
# capture output of script to pass info to applescript
# this is done to send the title of the post
var=$(python3 getstuff.py); osascript imessage.scpt "$var"
# 908-358-2293
