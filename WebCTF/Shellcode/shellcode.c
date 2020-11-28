#include <stdio.h>
#include <unistd.h>
#include <string.h>

// gcc -m32 shellcode.c -o shellcode -Wall -m32 -no-pie -fno-pie -z execstack -fno-stack-protector -Wl,-z,relro -mpreferred-stack-boundary=2

void prog();
void get_name(char *a1);

char buffer[1024];

int main() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);

  puts(
    "  _________.__           .__  .__                   .___      \n"
    " /   _____/|  |__   ____ |  | |  |   ____  ____   __| _/____  \n"
    " \\_____  \\ |  |  \\_/ __ \\|  | |  | _/ ___\\/  _ \\ / __ |/ __ \\ \n"
    " /        \\|   Y  \\  ___/|  |_|  |_\\  \\__(  <_> ) /_/ \\  ___/ \n"
    "/_______  /|___|  /\\___  >____/____/\\___  >____/\\____ |\\___  >\n"
    "        \\/      \\/     \\/               \\/           \\/    \\/ \n"
    "\n"
    "\n");
  prog();
  return 0;
}

void prog() {
  char v1[1008];
  get_name(&v1);
  printf("Hello Mr.%s\n", &v1);
}

void get_name(char *a1) {
  puts("What is your name?");
  read(0, buffer, 4096);
  memcpy(a1, buffer, 1024);
}
