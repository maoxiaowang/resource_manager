FROM nginx:1.25.4-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

# install dependencies
RUN rm /etc/apt/sources.list.d/* -f
ADD ./sources.list /etc/apt
RUN apt-get update && apt-get install -y --no-install-recommends gcc netcat iputils-ping tcpdump
