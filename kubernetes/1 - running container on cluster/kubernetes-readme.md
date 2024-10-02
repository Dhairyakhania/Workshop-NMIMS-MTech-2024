## Docker Revision
- Running a container `docker run -it ubuntu` or `docker run -it busybox`. Busy box is small size linux container = 5MB, ubuntu is larger in size = 78MB.
- Getting details of running containers `docker ps`
- Important commands - `ps, images, run, start, stop, build, pull, push, `


# Kubernetes Install Instructions
1. VSCode -> Extensions install  `Docker & Kubernetes extension`
2. VSCode -> Docker Extension -> Login to `hub.docker.com` & use private token to sign in from code space
2. Install minikube, For running Kubernetes locally, use minikube
3. Start minikube by running `minikube start`
4. Interact with kubernetes by command `kubectl `
5. Visual dashboard of running kubernetes clusters `minikube dashboard`


- kubectl apply -f pv.yaml
- kubectl apply -f statefulset.yaml
-  kubectl get pods
-  kubectl get statefulsets
-  kubectl get pv
-  kubectl get pvc
-  kubectl get services
-  kubectl get ingress
-  kubectl port-forward svc/flask-service 8080:80