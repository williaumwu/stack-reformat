#!/bin/bash

export DOCKER_BUILD_DIR=${DOCKER_BUILD_DIR:=/var/tmp/docker/build}
export DOCKER_FILE=${DOCKER_FILE:=Dockerfile}
export DOCKER_IMAGE_TAG=${DOCKER_IMAGE_TAG:=test}
export REPOSITORY_URI=${REPOSITORY_URI:=test}
export DOCKER_ENV_FIELDS=${DOCKER_ENV_FIELDS:=None}
export DOCKER_ENV_FIELDS_B64=${DOCKER_ENV_FIELDS_B64:=None}

# Build with custom image tag
cd $DOCKER_BUILD_DIR

ARGS=""

if [ $DOCKER_ENV_FIELDS == "None" ]
then
    BUILD_CMD="docker build -t $REPOSITORY_URI:$DOCKER_IMAGE_TAG . -f $DOCKER_FILE "
else
    for i in ${DOCKER_ENV_FIELDS//,/ }
    do
      j=$(eval echo $`eval 'echo "$i"'`)
      ARGS="--build-arg $i=$j $ARGS"
    done

    BUILD_CMD="docker build $ARGS -t $REPOSITORY_URI:$DOCKER_IMAGE_TAG . -f $DOCKER_FILE"
fi

echo "###############################################################"
echo "BUILD_CMD $BUILD_CMD"
echo "###############################################################"

$BUILD_CMD || exit 10

echo "###############################################################"
echo "# push $REPOSITORY_URI:$DOCKER_IMAGE_TAG"
echo "###############################################################"

docker push $REPOSITORY_URI:$DOCKER_IMAGE_TAG || exit 8
