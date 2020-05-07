

# Dockercon 2020: Labels Labels Labels

One underutilized, and amazing, thing about the docker image scheme is labels. Labels are a built in way to document all aspects about the image itself. Think about all the information that the tags inside your clothing carry. If you care to look you can find out everything about the garment. All that information can be very valuable. Now think about how we can leverage labels to carry similar information. We can even use the labels to contain Docker Compose or even Kubernetes Yaml. We can even include labels into the CI/CD process making things more secure and smoother. Come find out some fun techniques on how to leverage labels to do some fun and amazing things.


---

clemenko@clemenko compose % docker inspect clemenko/flask_demo | jq -r '.[].Config.Labels.“org.stack”'
dmVyc2lvbjogIjMuNCIKc2VydmljZXM6CiAgYXBwOgogICAgaW1hZ2U6IGNsZW1lbmtvL2ZsYXNrX2RlbW8KICAgIGRlcGxveToKICAgICAgcmVwbGljYXM6IDQKICAgICAgdXBkYXRlX2NvbmZpZzoKICAgICAgICBwYXJhbGxlbGlzbTogMgogICAgICBsYWJlbHM6CiAgICAgICAgICBjb20uZG9ja2VyLmxiLm5ldHdvcms6IGZsYXNrX2t2CiAgICAgICAgICBjb20uZG9ja2VyLmxiLmhvc3RzOiBhcHAuZG9ja3IubGlmZQogICAgICAgICAgY29tLmRvY2tlci5sYi5wb3J0OiA1MDAwCiAgICBwb3J0czoKICAgICAgLSA1MDAwOjUwMDAKICAgIG5ldHdvcmtzOgogICAgICBkYjoKICAgICAga3Y6CgogIG1vbmdvOgogICAgaW1hZ2U6IG1vbmdvCiAgICBuZXR3b3JrczoKICAgICAgZGI6CgogIHJlZGlzOgogICAgaW1hZ2U6IHJlZGlzOmFscGluZQogICAgbmV0d29ya3M6CiAgICAgIGt2OgoKbmV0d29ya3M6CiAga3Y6CiAgZGI6Cg==
clemenko@clemenko compose % echo “$(docker inspect clemenko/flask_demo | jq -r ‘.[].Config.Labels.“org.stack”‘| base64 -D)” |docker stack deploy -c- flask
Creating network flask_kv
Creating network flask_db
Creating service flask_mongo
Creating service flask_redis
Creating service flask_app


## Outline

### ME

### Schema
 - size
 - key=value

 Review : docker inspect clemenko/flask_demo | jq -r '.[].Config.Labels'

LABEL org.opencontainers.image.authors=$BUILD_SIGNATURE \
      org.opencontainers.image.source="https://github.com/clemenko/dc20_labels/tree/master/demo_flask" \
      org.opencontainers.image.created=$BUILD_DATE \
      org.opencontainers.image.title="clemenko/flask_demo" \
      org.opencontainers.image.description="The repository contains a simple flask application. flask --> mongo, flask --> redis." \
      org.opencontainers.image.build="docker build -t clemenko/flask_demo --build-arg BUILD_DATE=$(date +%D) --build-arg BUILD_VERSION=0.01 --build-arg COMPOSE=$(cat flask_compose.yml|base64)  --build-arg K8SYML=$(cat flask_k8s.yml|base64) --build-arg BUILD_SIGNATURE=clemenko@gmail.com . " \
      org.opencontainers.image.source=$BUILD_VERSION \
      org.opencontainers.image.healthz="/healthz" \
      org.zdocker.compose=$COMPOSE \
      org.zdocker.k8s=$K8SYML

### More Complex

### CI/CD completion

### Security Concerns
CVE
Required Image Label Policy

### Compose or Kube

### Demo

https://github.com/clemenko/rancher/blob/master/rancher.sh



