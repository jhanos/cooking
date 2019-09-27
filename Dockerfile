FROM alpine
RUN apk --update add python3 py3-yaml py3-jinja2 nginx && pip3 install mkdocs-material && mkdir /app /run/nginx
WORKDIR /src
COPY default.conf /etc/nginx/conf.d/default.conf
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT /entrypoint.sh
