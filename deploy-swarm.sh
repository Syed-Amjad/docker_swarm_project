#!/bin/bash

# Initialize Docker Swarm if not already
docker info | grep 'Swarm: active' > /dev/null || docker swarm init

# Deploy the stack
STACK_NAME=docker_showcase

echo "Deploying stack $STACK_NAME..."
docker stack deploy -c docker-stack.yml $STACK_NAME
