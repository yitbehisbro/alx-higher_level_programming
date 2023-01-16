#!/bin/bash
#Display the size of the body in byte
curl -sI "$1" | grep -i content-length | awk '{print $2}'
