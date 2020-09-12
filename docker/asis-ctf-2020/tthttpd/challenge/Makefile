all:
	gcc -Wno-unused-result -Wl,-z,now,-z,relro main.c -o tthttpd -fstack-protector -pie -O0
	mv tthttpd ../distfiles
