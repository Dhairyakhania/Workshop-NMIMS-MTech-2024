## Docker Revision
- Running a container `docker run -it ubuntu` or `docker run -it busybox`. Busy box is small size linux container. Busybox = 5MB, ubuntu is larger in size = 78MB.
    - Busybox vs Puppy Linux vs Tiny Core Linux vs Lubuntu 
- Getting details of running containers `docker ps`
- Important commands - `ps, images, run, start, stop, build, pull, push, `


## Lab 1: Using docker
Step 1: Installation
    Require docker buildx to build docker image
    - brew install docker-buildx for mac
    - apt install docker-buildx-plugin
    - yum install docker-buildx-plugin

Step 2: Building docker image
Run via `docker build --tag my-python-app .`
or build & run: `docker-compose up --build`

Step 3: Run docker
- start docker service by running `dockerd`
- Different ways of running: `docker run busybox` vs `docker run -it busybox` vs `docker run -d busybox`
- `docker run -d -p 80:80 first-docker-image`

Step 4: Upload docker image for public sharing
- `docker login`
- `docker --tag my-python-app first-docker-image`
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