#!/bin/bash
# This script sends a get request and also and displays the body of the response
response=$(curl -sI $1) && [[ "$response" == *"200 OK"* ]] && curl -s $1
