SHELL := /bin/bash
PROJECT_NAME = {{ cookiecutter.project_slug }}

DOCKER_IMG := $(PROJECT_NAME):latest
DOCKER_RUN := docker run --rm -v $(PWD):/opt -w /opt

guard-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "Missing '$*' variable"; \
		exit 1; \
	fi

help:
	@echo "usage: make <command> [VARIABLE=X.Y.Z]"
	@echo
	@echo "COMMANDS"
	@echo "    help     Show this help"
	@echo "    clean    Remove volumes and images"
	@echo "    build    Build docker image from Dockerfile"
	@echo "    shell    Enter into a shell of the docker container"
	@echo "    lint     Run all linters"
	@echo "    mypy     Run mypy linter"
	@echo "    flake8   Run flake8 linter"
	@echo "    bandit   Run bandit linter"
	@echo "    check    Run all tests"
	@echo "    check/?  Run a single test"
	@echo
	@echo "VARIABLES"
	@echo "    VERSION  Software version"
	@echo

clean:
	docker volume rm $(PROJECT_NAME) --force
	docker rmi $(DOCKER_IMG) --force

build:
	docker build -t $(DOCKER_IMG) .

shell: build
	$(DOCKER_RUN) -it $(DOCKER_IMG) bash

check: build
	$(DOCKER_RUN) $(DOCKER_IMG) python -B -m pytest -p no:cacheprovider --cov=$(PROJECT_NAME)

check/%: build
	$(DOCKER_RUN) $(DOCKER_IMG) python -B -m pytest -p no:cacheprovider $@

mypy:
	$(DOCKER_RUN) grktsh/mypy --cache-dir=/dev/null $(PROJECT_NAME) tests

flake8:
	$(DOCKER_RUN) alpine/flake8:3.5.0 $(PROJECT_NAME) tests

bandit:
	$(DOCKER_RUN) opensorcery/bandit -r $(PROJECT_NAME)

lint: mypy flake8 bandit
