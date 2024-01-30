# Klaster w chmurze (GCP)

## Google Kubernetes Engine

## Rejestracja

[Rejestracja Google Cloud](https://cloud.google.com/free)

### Instalacja gcloud CLI

[Dokumentacja Google](https://cloud.google.com/sdk/docs/install)

### Inicjalizacja gcloud CLI

[Dokumentacja Google](https://cloud.google.com/sdk/docs/initializing)

Polecenie: `gcloud config list`

zwraca aktualną konfigurację, np:

```
[core]
account = <email>@gmail.com
project = <id-projektu>

[compute]
zone = europe-central2-a
region = europe-central2
```

### Utworzenie klastra

[Dokumentacja Google](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster)

```
gcloud container clusters create-auto dev-cluster \
    --region europe-central2 \
    --project=kurs-kubernetesa

gcloud container clusters get-credentials dev-cluster \
    --region europe-central2 \
    --project=kurs-kubernetesa
```

### Dalsze kroki

[TLS Cert Manager](https://cert-manager.io/docs/tutorials/acme/nginx-ingress/)
