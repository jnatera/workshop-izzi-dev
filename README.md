# workshop-izzi-dev
Workshop sobre servicios de desarrollo

## Hacer deploy en kubernetes

## Cambiar al proyecto donde trabajaran

- a gcloud config set project ent-qas-project-id
- b gcloud config set project ent-dev-project-id
- c gcloud config set project ent-prd-project-id

- 1 Tomar el nombre del proyecto

`gcloud config get-value project`

- 2 Compilar la imagen

`gcloud builds submit --tag gcr.io/ent-dev-project-id/api-doc-factory-gke .`

- 3 Crear un cluster si no está creado

`gcloud container clusters create helloworld-gke --num-nodes 1 --zone your-gcp-zone`

- 4 Verifica que tienes acceso al cluster
  `kubectl get nodes`
- 5 Crear el archivo deployment.yaml
-
- 6. Hacer deploy en el cluster
     `kubectl apply -f deployment.yaml`
- 7 Ver estatus del deployment
  `kubectl get deployments`
- 8 Luego de completado vemos los pods creados
  `kubectl get pods`
- 9 Creamos el servicio
  `kubectl apply -f service.yaml`
- 10 Vemos los servicios creados
  `kubectl get services`

- 11 Eliminar la imagen del container registry
  `gcloud container images delete gcr.io/project-id/api-doc-factory-gke`
- 12 Revisar cuantas replicas existen
  `kubectl get replicasets`
- 13 Detalle de nuestro diployment
  `kubectl describe deployments api-docfactory-gke`
- 14 Verificar si el despliegue fue hecho correctamente
  `kubectl rollout status deployment api-docfactory-gke`
- 15 Deshacer el ultimo despliegue realizado
  `kubectl rollout undo deployment api-docfactory-gke`
- 16 Revisar logs para ver si inició el servicio doc factory+, colocar nombre del pod al final
  `kubectl logs api-docfactory-gke-55ddb8965d-fxvl9`
- 17 Acceder a la consola del pod del servicio
  `kubectl exec api-docfactory-gke-55ddb8965d-fxvl9 -ti bash`
- 18

## Probar el ingress

kubectl get ingress api-docfactory-gke --output yaml

gcloud compute addresses create docfactory-static-ip --global --project=ent-dev-project-id --region=us-east1
gcloud compute addresses describe docfactory-static-ip --global

`kubectl create secret tls "certificate-docfactory" --cert="certs\tsl.crt" --key="certs\tsl.key"`
kubectl get managedcertificate

otra forma
gcloud compute ssl-certificates create cert_df --description=test --domains=certificate-docfactory --global
gcloud compute ssl-certificates create certificate-docfactory --certificate certs\tsl.crt --private-key certs\tsl.key --domains=certificate-docfactory
gcloud compute ssl-certificates list --global

otra forma
kubectl create -f manifests\certificates.yaml
kubectl apply -f manifests\certificates.yaml
kubectl get app-name-backend.dev.cloud.prueba.com.mx
kubectl describe managedcertificate certificate-docfactory

```sh
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/ingress.yaml
```

Cluster
Detener cluster
gcloud dataproc clusters stop ent-qas-sedes-gke --region=us-east1-b
Iniciar cluster
gcloud dataproc clusters start ent-qas-sedes-gke --region=us-east1-b
