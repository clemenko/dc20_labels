FROM alpine

ARG BUILD_DATE
ARG BUILD_VERSION
ARG COMPOSE
ARG K8SYML

LABEL org.opencontainers.image.authors="clemenko@gmail.com" \
      org.opencontainers.image.source="https://github.com/clemenko/dockerfiles/tree/master/demo_flask" \
      org.opencontainers.image.created=$BUILD_DATE \
      org.opencontainers.image.title="clemenko/flask_demo" \
      org.opencontainers.image.description="The repository contains a simple flask application " \
      org.opencontainers.image.build="docker build -t clemenko/flask_demo --build-arg BUILD_DATE=$(date +%D) --build-arg BUILD_VERSION=0.01 --build-arg COMPOSE=$(cat ../../compose/flask_demo.yml|base64)  --build-arg K8SYML=$(cat ../../k8s_yaml/k8s_all_the_things.yml|base64) . " \
      org.opencontainers.image.source=$BUILD_VERSION \
      org.opencontainers.image.healthz="/healthz"
      org.zdocker.compose=$COMPOSE \
      org.zdocker.k8s=$K8SYML

RUN apk -U upgrade && apk add --no-cache python3 curl  &&\
    pip3 install --no-cache-dir --upgrade pip &&\
    pip3 install --no-cache-dir flask redis pymongo &&\
    #apk --purge del apk-tools &&\
    rm -rf /var/cache/apk/*
    
WORKDIR /code
ADD . /code
EXPOSE 5000
HEALTHCHECK CMD curl -f http://localhost:5000/healthz || exit 1
CMD ["python3", "app.py"]
