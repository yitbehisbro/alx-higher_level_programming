#!/bin/bash
#Display possible list of methods
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
