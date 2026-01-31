FROM nginx:alpine

# Copy static assets
COPY index.html /usr/share/nginx/html/index.html

# Copy entrypoint script
COPY entrypoint.sh /docker-entrypoint.d/40-env-config.sh
RUN chmod +x /docker-entrypoint.d/40-env-config.sh

# Expose port 80
EXPOSE 80

# Nginx default entrypoint automatically runs scripts in /docker-entrypoint.d/
CMD ["nginx", "-g", "daemon off;"]
