#!/bin/sh

# Create config file with environment variable
echo "window.ENV = {" > /usr/share/nginx/html/env-config.js
echo "  VITE_API_URL: \"${VITE_API_URL}\"" >> /usr/share/nginx/html/env-config.js
echo "};" >> /usr/share/nginx/html/env-config.js

# Start Nginx
exec "$@"
