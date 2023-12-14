#!/bin/bash

apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu jammy stable"
apt-cache policy docker-ce
apt-get install docker-ce -y
