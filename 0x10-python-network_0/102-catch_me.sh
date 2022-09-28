#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:School"
