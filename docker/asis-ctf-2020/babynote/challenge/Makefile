all:
	gcc -Wl,-z,now,-z,relro main.c -o chall -fstack-protector -pie -O0
	mv chall ../distfiles
	cp /lib/x86_64-linux-gnu/libc-2.27.so ../distfiles
