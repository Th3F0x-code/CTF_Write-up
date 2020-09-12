#include <stdio.h>
#include <string.h>
#include <unistd.h>

int readline(char *buf, int size) {
  int len;
  gets(buf);
  len = strlen(buf);
  if (len >= size) {
    puts("[FATAL] Buffer Overflow");
    _exit(1);
  }
  return len;
}

int main(void) {
  char buf[0x40] = {0};
  while(1) {
    if (readline(buf, 0x40) == 0) break;
    printf(buf);
    putchar('\n');
  }
  return 0;
}

__attribute__((constructor))
void setup(void) {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  alarm(60);
}
