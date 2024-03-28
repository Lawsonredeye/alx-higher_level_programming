#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
request=$(curl -sI $1) && allow=$(echo "$request" | grep "Allow") && echo $allow
