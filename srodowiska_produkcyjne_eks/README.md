# Klaster w chmurze (AWS)

## Elastic Kubernetes Service

## Rejestracja

[Rejestracja](https://aws.amazon.com/free)

### Instalacja AWS CLI

[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

### Inicjalizacja AWS CLI

[Dokumentacja](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

Polecenie: `aws configure`

Tworzy następujące pliki (domyślny profile, można mieć ich kilka):

`cat ~/.aws/config`

```
[default]
region = eu-central-1
```

`cat ~/.aws/credentials`

```
[default]
aws_access_key_id = <accesss-key>
aws_secret_access_key = <access-secret-key>
```

Należy pamiętać, że w dłużej perspektywie nie jest zalecane trzymanie credentials jako plain text.

W tym celu w organizacjach używa się SSO natomiast prywatnie można użyć narzędzi typu [AWS Vault](https://github.com/99designs/aws-vault)

### eksctl - oficjalne CLI do zarządzania EKS

[GitHub eksctl](https://github.com/eksctl-io/eksctl/tree/main)

[Dokumentacja eksctl](https://eksctl.io/usage/creating-and-managing-clusters/)

### Tworzenie klastra z wykorzystaniem eksctl

```
eksctl create cluster -f simple-cluster.yaml
```

### Przykłady konfiguracji eksctl

[ekctl przykłady](https://github.com/eksctl-io/eksctl/tree/main/examples)

### Dalsze kroki

[TLS Cert Manager](https://cert-manager.io/docs/tutorials/acme/nginx-ingress/)

### Usunięcie klastra

`eksctl delete cluster --name kurs-kubernetesa`
