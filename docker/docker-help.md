Require docker buildx to build docker image
- brew install docker-buildx for mac
- apt install docker-buildx-plugin
- yum install docker-buildx-plugin

Run via `docker buildx build --tag my-python-app .`

- `docker login`
- start docker by running `dockerd`
- `docker tag my-python-app first-docker-image`
- `docker push              first-docker-image`
- `docker pull first-docker-image`
- `docker run -d -p 80:80 first-docker-image`