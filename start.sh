#!/bin/sh

# Create/Update database schema
flask db upgrade

# Start API Server
exec python app.py