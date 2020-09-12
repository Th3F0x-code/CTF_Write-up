#ifndef __CREDMGR_H
#define __CREDMGR_H

#define DEVICE_NAME "note"
#define MAX_NOTE_SIZE 0x80
#define CMD_ALLOC  0xc12ed001
#define CMD_DELETE 0xc12ed002
#define CMD_STORE  0xc12ed003
#define CMD_LOAD   0xc12ed004

typedef struct {
  unsigned int size;
  unsigned char *note;
} Command;

#endif
