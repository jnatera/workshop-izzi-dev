# Python flask for Kubernetes

docker build -t kube-app .

docker run -e PORT 8080  -p 8080:8080 kube-app