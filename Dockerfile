FROM alpine
RUN apk --update add python3 py3-flask py3-yaml
CMD python3 /app/app.py
