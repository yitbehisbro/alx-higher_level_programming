#!/bin/bash
# Script that makes a request to causes an specific response
curl -sX PUT -L -d --header "origin: You got me!" 0.0.0.0:5000/catch_me
