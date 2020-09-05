#!/bin/bash

# shellcheck disable=SC2028
echo "1. Start\n"
# shellcheck disable=SC2028
echo "2. Stop\n"
# shellcheck disable=SC2162
read xx

if [ $xx -eq 1 ]; then
  sudo wg-quick up "$PWD/profile.conf"
else
  sudo wg-quick down "$PWD/profile.conf"
fi
