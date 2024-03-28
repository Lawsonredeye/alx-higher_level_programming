#!/bin/bash
# This script fetches the content length of a request made
curl -sI $1 | awk '/Content-Length/ {print $2}'
