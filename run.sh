#!/bin/bash

bash ./build.sh
docker run --rm --name inversity-provisioner-container -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock inversity-provisioner

