FROM alpine

ARG BUILD_DATE
ARG BUILD_VERSION
ARG BUILD_ID
ARG BUILD_NUMBER
ARG GIT_COMMIT
ARG BUILD_SIGNATURE
ARG JENKINS_URL
ARG COMPOSE
ARG K8SYML

LABEL org.opencontainers.image.authors=$BUILD_SIGNATURE \
      org.opencontainers.image.source="https://github.com/clemenko/dc20_labels/tree/master/demo_flask" \
      org.opencontainers.image.created=$BUILD_DATE \
      org.opencontainers.image.build_id=$BUILD_ID \
      org.opencontainers.image.build_number=$BUILD_NUMBER \
      org.opencontainers.image.commit=$GIT_COMMIT \
      org.opencontainers.image.build=$JENKINS_URL \
      org.opencontainers.image.title="clemenko/flask_demo" \
      org.opencontainers.image.description="The repository contains a simple flask application. flask --> mongo, flask --> redis." \
      org.opencontainers.image.build="docker build -t clemenko/flask_demo --build-arg BUILD_DATE='$(date +%D)' --build-arg BUILD_VERSION='0.1' --build-arg COMPOSE='$(cat flask_compose.yml|base64)' --build-arg K8SYML='$(cat flask_k8s.yml|base64)' --build-arg BUILD_SIGNATURE='clemenko@gmail.com' --build-arg JENKINS_URL='jenkins' --build-arg BUILD_ID=$BUILD_ID --build-arg BUILD_NUMBER=$BUILD_NUMBER --build-arg GIT_COMMIT=$GIT_COMMIT . " \
      org.opencontainers.image.source=$BUILD_VERSION \
      org.opencontainers.image.healthz="/healthz" \
      org.zdocker.compose=$COMPOSE \
      org.zdocker.k8s=$K8SYML

RUN apk -U upgrade && apk add --no-cache python3 curl  &&\
    pip3 install --no-cache-dir --upgrade pip &&\
    pip3 install --no-cache-dir flask redis pymongo &&\
    apk --purge del apk-tools &&\
    rm -rf /var/cache/apk/*
    
WORKDIR /code
ADD . /code
EXPOSE 5000
HEALTHCHECK CMD curl -f http://localhost:5000/healthz || exit 1
CMD ["python3", "app.py"]
