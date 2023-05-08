# system python interpreter. used only to create virtual environment
PY = python3
VENV = venv
BIN=$(VENV)/bin

# make it work on windows too
ifeq ($(OS), Windows_NT)
    BIN=$(VENV)/Scripts
    PY=python
endif

$(VENV): requirements.txt
	$(PY) -m venv $(VENV)
	$(BIN)/pip install --upgrade -r requirements.txt
	touch $(VENV)

docker-build:
	docker build -t app .

minikube-build:
	minikube image build -t app:1.0.0 .

minikube-build-1.1.0:
	minikube image build -t app:1.1.0 .

minikube-list-images:
	minikube image ls
