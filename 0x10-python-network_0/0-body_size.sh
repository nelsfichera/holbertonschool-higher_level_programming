#!/bin/bash
#gets the body size of response
curl -sI "$1"| grep Content-Length | awk '{print $2}'
