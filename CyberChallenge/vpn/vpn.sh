#!/bin/bash

echo "1. Start\n"
echo "2. Stop\n"
read xx

if [ $xx -eq 1 ]
then
	sudo wg-quick up "$PWD/profile.conf"
else
	sudo wg-quick down "$PWD/profile.conf"
fi
