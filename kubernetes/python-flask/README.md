# Python flask for Kubernetes

docker build -t kube-app .

docker run -e PORT=8080  -p 8080:8080 kube-app

GOOGLE_CLOUD_PROJECT=innate-bonfire-361004
LOCATION=us-central1

gcloud container clusters create cluster-gke --num-nodes 1 --zone $LOCATION

gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/python-flask-nombre-gke .

kubectl apply -f gke/dev/1-deployment.yaml

kubectl get deployments -w
kubectl delete deployments --all

kubectl apply -f gke/dev/2-service.yaml
kubectl get services

kubectl apply -f gke/dev/3-ingress.yaml

skaffold run -f skaffold.yaml