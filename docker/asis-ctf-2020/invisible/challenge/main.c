#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#define MAX_SIZE 120
char *ptr[2];

void handler(int sig) {
  puts("[-] timeout");
  exit(0);
}

int readline(const char *msg, char *buf, int size) {
  int s;
  char *p;
  printf("%s", msg);
  if ((s = read(0, buf, size)) <= 0) exit(0);
  if (p = strchr(buf, '\n')) *p = 0;
  return s;
}
int readint(const char *msg) {
  char buf[16];
  readline(msg, buf, 15);
  return atoi(buf);
}

void new(void) {
  unsigned short size, index;
  if ((index = readint("index: ")) > 1 || ptr[index]) goto ERROR;
  if ((size = readint("size: ")) > MAX_SIZE) goto ERROR;
  ptr[index] = malloc(size);
  if (ptr[index] == NULL) goto ERROR;
  size = readline("data: ", ptr[index], size-1);
  ptr[index][size] = 0;
  puts("[+] new: done");
  return;
 ERROR:
  puts("[-] new: error");
  return;
}
void edit(void) {
  unsigned short size, index;
  if ((index = readint("index: ")) > 1 || ptr[index] == NULL) goto ERROR;
  if ((size = readint("size: ")) > MAX_SIZE) goto ERROR;
  if (realloc(ptr[index], size) == NULL) goto ERROR;
  size = readline("data: ", ptr[index], size-1);
  ptr[index][size] = 0;
  puts("[+] edit: done");
  return;
 ERROR:
  puts("[-] edit: error");
  return;
}
void delete(void) {
  unsigned short index;
  if ((index = readint("index: ")) > 1 || ptr[index] == NULL) goto ERROR;
  free(ptr[index]);
  ptr[index] = NULL;
  puts("[+] delete: done");
  return;
 ERROR:
  puts("[-] delete: error");
  return;
}

int main(void) {
  while(1) {
    switch(readint("1. new\n2. edit\n3. delete\n> ")) {
    case 1: new(); break;
    case 2: edit(); break;
    case 3: delete(); break;
    default: puts("Bye."); return 0;
    }
  }
}

__attribute__((constructor))
void setup(void) {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  signal(SIGALRM, handler);
  alarm(180);
}
