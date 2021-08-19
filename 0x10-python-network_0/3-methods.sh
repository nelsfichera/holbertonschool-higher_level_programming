#!/bin/bash
#shows allowed verbs at given ip
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{print $2}'
