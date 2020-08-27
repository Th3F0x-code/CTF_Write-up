#!/bin/bash
# In the name of Allah

server='69.172.212.23'
task='babynote'
base_path='/home/rooney/Documents/asis-repos/quals2020-pwn'

rsync -a -rtuv --exclude solution/ --exclude $task/ --exclude README.md --exclude=*.txz \
	--exclude docker-compose.yml --exclude make_ctf_archive.sh --exclude sync.sh --exclude .DS_Store --delete-excluded \
	$base_path/$task/ root@$server:/root/apps/pwn/$task/