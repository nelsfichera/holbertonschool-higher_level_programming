#!/bin/bash
#Catches the page 
curl -s 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -L -H "Origin: HolbertonSchool"
