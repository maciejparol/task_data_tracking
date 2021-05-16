# STAGE 1
FROM nginx:1.20.0-alpine
COPY nginx/docker.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
