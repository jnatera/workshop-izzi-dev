# workshop

gcloud auth application-default \
    login

gcloud spanner samples init \
    finance --instance-id \
    workshop

export GOOGLE_APPLICATION_CREDENTIALS=./application_default_credentials.json
export GOOGLE_CLOUD_PROJECT=innate-bonfire-361004

# Instalamos paquetes
pip install django-google-spanner
pip install django~=3.2
py manage.py migrate


# Comandos Spanner

$ gcloud spanner instances create django-test-instance --config=regional-us-central1 --description="Django Test Instance" --nodes=1
$ gcloud spanner databases create django-test-db --instance django-test-instance

gcloud spanner databases execute-sql django-test-db --instance workshop --sql "select TABLE_NAME, TABLE_TYPE, SPANNER_STATE from information_schema.tables"

kubectl create secret generic polls-secret --from-env-file=.env

gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/django-spanner-nombre-gke .



# LOGGING
gcloud logging write my-test-log "A simple entry."
gcloud logging write --payload-type=json my-test-log '{ "message": "My second entry", "weather": "partly cloudy"}'
gcloud logging read "resource.type=global"
jsonPayload.weather:partly

{
  "projectIds": [
    string
  ],
  "resourceNames": [
    string
  ],
  "filter": string,
  "orderBy": string,
  "pageSize": integer,
  "pageToken": string
}

gcloud logging logs delete my-test-log