## Docker Revision
- Running a container `docker run -it ubuntu` or `docker run -it busybox`. Busy box is small size linux container. Busybox = 5MB, ubuntu is larger in size = 78MB.
    - Busybox vs Puppy Linux vs Tiny Core Linux vs Lubuntu 
- Getting details of running containers `docker ps`
- Important commands - `ps, images, run, start, stop, build, pull, push, `
- Running a demo container: `docker run busybox` vs `docker run -it busybox` vs `docker run -d busybox`
- Running a demo container: `docker run ubuntu` vs `docker run -it ubuntu` vs `docker run -d ubuntu`

## Installation
- Install docker extension in vscode
- Install docker buildx for building custom docker image
    - brew install docker-buildx for mac
    - apt install docker-buildx-plugin
    - yum install docker-buildx-plugin


## Lab 1: Build & run docker
- Step 1: Building docker image - `docker build . --tag first-docker-image`
- Step 2: Run docker container - `docker run -d -p 5000:5000 first-docker-image` or `docker run -d -p 127.0.0.1:5000:5000 first-docker-image`. Port numbers must match at all 3 places. Dockerfile, Python Source Code & Docker Run command

Running a TODO webapp
- `git clone https://github.com/docker/getting-started-app.git`
- `docker build -t getting-started .`
- `docker run -d -p 127.0.0.1:3000:3000 getting-started`

## Lab 2: Docker Hub for uploading images
- Create account on docker hub. 
- [Create a personal access token](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/unauthorized-docker-create-access-token-dockerhub-incorrect-username-password) 
- `docker login -u ajinkyakolhe112`. Copy the personal access token you created, not the password.
- `docker build . --tag ajinkyakolhe112/simple_docker_image`
- `docker push ajinkyakolhe112/simple_docker_image`

### Lab 3: Running Docker using Docker compose
- Step 1: Build a YAML file which has all the commands we manually execute to create docker container. `docker-compose.yaml`
- Step 2: Build & Run in one command using `docker-compose up --build`. Entire container will be built just by executing this single command


### Lab 4: Creating folders in docker container to save data
Docker has two types of folder sharing. 
1. `Volume mount`: This allows to save runtime data of container into a folder. So this data can be used even after container shuts down.
2. `Bind mount`: This allows container to see a specific folder on host's file system.. Any changes to the folder, is immediately reflected in the container's `bind mount`

#### Volume Mount Lab
- `docker build . -t volumes_container`
- `docker run -v local_directory:/mounted_directory_in_container -p5000:5000 volumes_container`
- check if folder's content is read by flask api
- change file content and see if flask api reads updated file contet.
- alternative `docker-compose up --build`

##### Bind Mount Lab