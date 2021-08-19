#!/bin/bash
#returns status code of get response
curl -s -o /dev/null -w "%{http_code}" "$1"
