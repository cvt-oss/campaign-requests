#!/bin/sh
set -e

# Wait for db startup
sleep 2

exec python run.py
