#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s -X POST -d "email={{EMAIL}}" -d "subject=I will always be here for PLD" $1
