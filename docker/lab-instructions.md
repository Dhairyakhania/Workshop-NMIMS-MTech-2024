## Lab 1: Using docker
Step 1: Installation
    Require docker buildx to build docker image
    - brew install docker-buildx for mac
    - apt install docker-buildx-plugin
    - yum install docker-buildx-plugin

Step 2: Building docker image
Run via `docker buildx build --tag my-python-app .` 
or `docker build --tag myflaskapp:latest .`

Step 3: Login & run docker
- `docker login`
- start docker by running `dockerd`
- `docker run -d -p 80:80 first-docker-image`

Step 4: Upload docker image for public sharing
- `docker tag my-python-app first-docker-image`
- `docker push              first-docker-image`
- `docker pull first-docker-image`

### Lab 2: Running Docker using Docker compose
Step 1: Build a YAML file which has all the commands we manually execute to create docker container. `docker-compose.yaml`

Step 2: Run using `docker-compose up --build`. Entire container will be built just by executing this single command


### Lab 3: Creating Docker Volumes
Step 1: Create Volume . a Storage space on docker container
- `docker volume create myvolume`

- docker run -v myvolume:/docker-data --rm -i -t busybox sh -c 'echo "World" > /docker-data/message.txt' 
- `docker-compose up --build`