#!/bin/bash

set -x

# Find all challenge directories
challenges=($(find . -maxdepth 1 -type d -name "*" -exec basename {} \;))

# Build the challenge and judge images
for challenge in "${challenges[@]}"; do
  docker build -t ${challenge}/challenge ./${challenge}/challenge
  docker build -t ${challenge}/judge ./${challenge}/judge
done

# Build the main app image
docker build -t inversity-provisioner .

