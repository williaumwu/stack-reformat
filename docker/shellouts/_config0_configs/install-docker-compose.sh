#!/bin/bash

export VERSION=1.13.0
curl -o /usr/local/bin/docker-compose -L "https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-$(uname -s)-$(uname -m)"
chmod +x /usr/local/bin/docker-compose
