FROM alpine:3.15

ADD ./install /install

RUN apk update --no-cache > /dev/null \
    && echo "**** install packages ****" \
    && apk add --no-cache curl tar bash openjdk15 python3 py3-pip > /dev/null \
    && pip3 install --upgrade pip > /dev/null \
    && pip3 install -r /install/requirements.txt > /dev/null \
    && bash /install/install-app.sh \
    && echo "**** cleanup ****" \
    && rm -rf /tmp/* /var/tmp/*

ENV LOG_LEVEL='error'

ADD ./app /app

VOLUME /data

CMD ["python", "-i", "/app/pyspark_shell.py"]
