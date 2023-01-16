#!/bin/bash
#Display the size of the body in byte
curl -sI "$1" | grep "Content-Length:" | awk '{print $2}'
