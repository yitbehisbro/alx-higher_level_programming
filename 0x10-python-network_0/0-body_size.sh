#!/bin/bash
#Display the size of the body in byte
curl -sI "$1" | grep content-length | cut -d " " -f 2
