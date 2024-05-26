# FROM nginx:1.25.4-alpine3.18 
FROM python:3.12.3-alpine3.20
WORKDIR /usr/src/app
COPY . /usr/src/app/
