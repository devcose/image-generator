#!/bin/sh
exec gunicorn -b :5000 main:app
