#!/bin/bash

bash ./build.sh
docker stop inversity-provisioner-container
docker rm inversity-provisioner-container
docker run --rm --name inversity-provisioner-container -p 127.0.0.1:8080:8080 -v /var/run/docker.sock:/var/run/docker.sock inversity-provisioner
