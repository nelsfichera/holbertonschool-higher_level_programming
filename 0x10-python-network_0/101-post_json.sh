#!/bin/bash
#sends post req using data from json file
curl -s "$1" --data @"$2" -H "Content-Type:application/json"
