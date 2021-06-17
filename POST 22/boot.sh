#!/bin/sh
# this script is used to boot a Docker container
# while true; do
#     flask db upgrade
#     if [[ "$?" == "0" ]]; then
#         break
#     fi
#     echo Deploy command failed, retrying in 5 secs...
#     sleep 5
# done
flask db upgrade
exec gunicorn -b :5000 inicio:app
