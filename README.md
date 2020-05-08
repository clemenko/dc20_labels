# Dockercon 2020: Labels Labels Labels

## Abstract

One underutilized, and amazing, thing about the docker image scheme is labels. Labels are a built in way to document all aspects about the image itself. Think about all the information that the tags inside your clothing carry. If you care to look you can find out everything about the garment. All that information can be very valuable. Now think about how we can leverage labels to carry similar information. We can even use the labels to contain Docker Compose or even Kubernetes Yaml. We can even include labels into the CI/CD process making things more secure and smoother. Come find out some fun techniques on how to leverage labels to do some fun and amazing things.

## Outline

### ME

### Why

Containers have the ability to carrying their own metadata. We can use the labels to add a lot of value to the image itself. The types of metadata are almost seamless. Think about the idea of a self documenting image. And even an image that has the information about how to deploy with Compose or Kubernetes.

### Schema

Review size constraints

Labels have a key=value structure. Quite simply you can set ANY key and ANY value. There are some good examples of what to use : https://github.com/opencontainers/image-spec/blob/master/annotations.md

Here are some examples of labels I like to use.

"org.opencontainers.image.authors": "clemenko@gmail.com",
"org.opencontainers.image.source": "https://github.com/clemenko/dc20_labels/tree/master/demo_flask",
"org.opencontainers.image.build": "docker build -t clemenko/flask_demo..." ,
"org.opencontainers.image.build_number": 22,
"org.opencontainers.image.build.server": http://jenkins.dockr.life/ \
"org.opencontainers.image.commit": "98c997f",
"org.opencontainers.image.created": "05/07/20",
"org.opencontainers.image.description": "The repository contains a simple flask application. flask --> mongo, flask --> redis.",
"org.opencontainers.image.healthz": "/healthz",
"org.opencontainers.image.version": "0.1",
"org.opencontainers.image.title": "clemenko/flask_demo",
"org.zdocker.compose": ... ,
"org.zdocker.k8s": ...

Labels can be retrieved with with a `docker pull` and `docker inspect clemenko/flask_demo | jq -r '.[].Config.Labels'`. Or Redhat has a neat too called Skopeo - https://github.com/containers/skopeo 
`skopeo inspect docker://docker.io/clemenko/flask_demo | jq .Labels`

### More Complex

Here is where it can get real interesting. What if we encoded the Docker Compose or Kubernetes yamls? What if we could use a single image to manage an entire stack? Here are two examples for using a label to deploy a stack.

```bash
#Compose
echo “$(docker inspect clemenko/flask_demo | jq -r '.[].Config.Labels."org.zdocker.compose"'| base64 -D)" |docker stack deploy -c- flask

#Kuberntes
echo "$(docker inspect clemenko/flask_demo | jq -r '.[].Config.Labels."org.zdocker.k8s"'| base64 -D)" | kubectl apply -f -
```

We can now combine the use of `skopeo` and the labels to pull the labels from remote images.

### CI/CD completion

There are several labels than should be updated during the CI process. Labels like `org.opencontainers.image.commit` can be VERY useful for tracing back the image to the exact commit to version control. `org.opencontainers.image.build_number` is also useful for tracking the image back to the build number on the build server. And don't forget to include the build server itself at `org.opencontainers.image.build.server`.

Having image provenance is vital to creating a Secure Supply Chain.

### Security Concerns

One real advantage of using the labels for CI is traceability. We can couple this with a good CVE scanner to provide real feedback to developers about their images. There are some container security platforms that can even create policies to prevent images from deploying that do not include the labels.

Required Image Label Policy

### Demo

Dockerfile
Jenkins
SR

### Demo Env

My k8s environment is:

- digitalocean/ubuntu/k3s - https://github.com/clemenko/rancher/blob/master/rancher.sh
- traefik ingress - https://github.com/clemenko/k8s_yaml/blob/master/traefik_crd_deployment.yml
- StackRox - https://github.com/clemenko/rancher/blob/master/rancher.sh#L211
- StackRox Traefik Ingress Route - https://github.com/clemenko/k8s_yaml/blob/master/stackrox_traefik_crd.yml
- jenkins - https://github.com/clemenko/k8s_yaml/blob/master/jenkins.yaml
- jenkins build pipeline job - https://github.com/clemenko/dc20_labels/blob/master/jenkins_pipeline.yml