#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void readline(const char *msg, char *buf, int size) {
  char *ptr;
  printf("%s", msg);
  if (read(0, buf, size) <= 0) exit(1);
  if (ptr = strchr(buf, '\n')) *ptr = '\0';
}
int readuint(const char *msg) {
  char buf[16];
  readline(msg, buf, 15);
  int a = atoi(buf);
  if (a < 0) exit(1);
  return a;
}
int menu() {
  puts("1. new");
  puts("2. show");
  puts("3. delete");
  return readuint("> ");
}

void new(char **notes, unsigned short n) {
  unsigned short index = (unsigned short)readuint("index: ");
  if (index >= n) return;
  unsigned short size = (unsigned short)readuint("size: ");
  if (size > 0x40) return;
  if ((notes[index] = calloc(1, size)) == NULL) return;
  readline("data: ", notes[index], size);
  puts("[+] created!");
}

void delete(char **notes, unsigned short n) {
  unsigned short index = (unsigned short)readuint("index: ");
  if (index >= n) return;
  if (notes[index] == NULL) return;
  free(notes[index]);
  notes[index] = NULL;
  puts("[+] deleted!");
}

void show(char **notes, unsigned short n) {
  unsigned short index = (unsigned short)readuint("index: ");
  if (index >= n) return;
  if (notes[index] == NULL) return;
  printf("[+] data: %s\n", notes[index]);
}

void note(short n) {
  char **notes = (char**)alloca(n * sizeof(char*));
  while(1) {
    switch(menu()) {
    case 1: new(notes, n); break;
    case 2: show(notes, n); break;
    case 3: delete(notes, n); break;
    default: puts("bye!"); return;
    }
  }
}

int main(void) {
  short n = (short)readuint("n: ");
  note(n);
}

__attribute__((constructor))
void setup(void) {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  alarm(60);
}
