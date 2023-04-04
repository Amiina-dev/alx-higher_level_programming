#!/bin/bash
#Takes a url, sends a request, and display the size of body of the response
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
