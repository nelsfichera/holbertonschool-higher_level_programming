#!/bin/bash 
#sends post to passed url and displays body of response
curl -s "$1" -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD'
