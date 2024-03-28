#!/bin/bash
# This script sends a get request and also and displays the body of the response
response=$(curl -sI $1)
if [[ "$response" == *"200 OK"* ]]
then
    curl -s $1
fi
