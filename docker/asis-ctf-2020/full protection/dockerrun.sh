#!/bin/sh
# In the name of Allah
 
for c in `docker ps -a | grep 'babynote\|Created\|127.0.0.1:491' | awk '{print $1}'`; do
	docker rm -f $c
done

docker images | grep none | awk '{print $3}' | xargs -I mm docker rmi -f mm

docker_port=9001
 
for port in `seq 49100 49100`; do
	docker run -dit --restart always -p 127.0.0.1:$port:$docker_port babynote
done
 
