#!/bin/sh
# this script is used to boot a Docker container

exec gunicorn -b :5000 inicio:app
