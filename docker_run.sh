#!/bin/bash

set -e

DOCKER_IMAGE_NAME="pr-world-covid"
DOCKER_TAG_NAME="latest"
DOCKER_CPUS="2"
DOCKER_MEMORY="3g"
DOCKER_MEMORY_SWAP="4g"
PROJECT_ROOT=$(pwd)
AWS_CREDENTIAL_FILE=".aws/credentials"

if [[ $(docker images | grep $DOCKER_IMAGE_NAME) == "" ]]; then
  ./docker_build.sh
fi

# shellcheck disable=SC2068
docker run -v ~/$AWS_CREDENTIAL_FILE:/root/$AWS_CREDENTIAL_FILE \
--cpus=$DOCKER_CPUS --memory=$DOCKER_MEMORY --memory-swap=$DOCKER_MEMORY_SWAP \
-it -v $PROJECT_ROOT:/app/ $DOCKER_IMAGE_NAME:$DOCKER_TAG_NAME $@
