#!/bin/bash
#Display status number only
curl -so /dev/null -w "%{http_code}" "$1"
