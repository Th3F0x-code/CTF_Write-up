#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include <syslog.h>

int max_keep_alive_requests = 2;

void readline(char *buf) {
  char c;
  char *ptr;
  for(ptr = buf; ; ++ptr) {
    if ((c = fgetc(stdin)) == EOF) break;
    if ((c == '\n') && (*(ptr-1) == '\r')) {
      *(ptr-1) = '\0';
      break;
    }
    *ptr = c;
  }
}

int filesize(FILE *fp) {
  fseek(fp, 0, SEEK_END);
  return ftell(fp);
}

void dumpfile(FILE *fp, const char *url) {
  char c;
  fseek(fp, 0, SEEK_SET);
  while((c = fgetc(fp)) != EOF) {
    fputc(c, stdout);
  }
}

void respfile(const char *filepath, int stcode, const char *ststr) {
  FILE *fp = fopen(filepath, "rb");
  syslog(LOG_DEBUG, filepath);

  if (fp) {
    printf("HTTP/1.1 %d %s\r\nContent-Length: %d\r\n\r\n",
           stcode, ststr, filesize(fp));
    dumpfile(fp, filepath);
  } else {
    if (stcode == 404) {
      fp = fopen("./error/500.html", "rb");
      if (fp) {
        printf("HTTP/1.1 500 Internal Server Error\r\nContent-Length: %d\r\n\r\n",
               filesize(fp));
        dumpfile(fp, filepath);
      } else {
        _exit(1);
      }
    } else {
      respfile("./error/404.html", 404, "Not Found");
    }
  }

  if (fp) fclose(fp);
}

int handle_request(char *request, char *path) {
  int i, keep_alive = 0;
  char *url, *p;

  memset(path, 0, 0x100);
  memset(request, 0, 0x100);
  strcpy(path, "./docroot");

  readline(request);
  if (strcmp(strtok(request, " "), "GET")) {
    respfile("./error/405.html", 405, "Not Allowed");

  } else {
    if ((url = strtok(NULL, " ")) == NULL) _exit(1);
    if (strstr(url, "..")) {
      respfile("./error/666.html", 666, "You Are Hacker");
      _exit(1);
    }
    if (*url != '/') _exit(1);
    if (*(url+1) == '\0') {
      strcat(url, "index.html");
    }

    int len = strlen(url);
    for(i = 0; i < len; i++) {
      path[9+i] = url[i];
    }

    do {
      readline(request);
      for (p = request ; *p; ++p) *p = tolower(*p);
      if (strtok(request, ":")) {
        if (strcmp(request, "connection") == 0) {
          if (strcmp(strtok(NULL, ""), " keep-alive") == 0) {
            keep_alive = 1;
          }
        }
      }
    } while(*request != '\0');

    respfile(path, 200, "OK");
  }

  return keep_alive;
}

void setup() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  openlog("tthttpd", LOG_PID, LOG_USER);
  alarm(30);
}

int main(void) {
  int i;
  char request[0x800], path[0x800];

  setup();
  for(i = 0; i < max_keep_alive_requests; i++) {
    if (!handle_request(request, path)) break;
  }
  closelog();
  _exit(0);
}
