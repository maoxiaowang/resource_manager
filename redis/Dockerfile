FROM harbor.service.hurwa-xian.consul:5000/library/redis:7.2.2

# create the app user
RUN addgroup --system redis && adduser --system --group redis

# make redis log directory
RUN mkdir -p /var/log/redis && mkdir -p /var/lib/redis

# change to the app user
RUN chown redis:redis /var/log/redis && chown redis:redis /var/lib/redis

# change user
USER redis

COPY redis.conf /etc/redis/redis.conf
