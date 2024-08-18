#!/bin/bash

bash ./build.sh
docker rm inversity-provisioner-container && sleep 3
docker run --rm --name inversity-provisioner-container -p 127.0.0.1:8080:8080 -v /var/run/docker.sock:/var/run/docker.sock inversity-provisioner