// gcc -g -O0 -Wl,-z,relro,-z,now -no-pie -o chall chall.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char *ptr;

void initialize() {
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);
}

void printmenu() {
  puts("1. add");
  puts("2. view");
  puts("3. delete");
  puts("4. quit");
}

void add() {
  int size;
  puts("enter the size");
  scanf("%d", &size);
  if (size < 0x100) {
    ptr = malloc(size);
    puts("Enter data");
    read(0, ptr, size);
  }
}

void view() {
  puts("Printing the data inside");
  puts(ptr);
}

void delete() {
  puts("Deleting...");
  free(ptr);
}

int main() {
  int choice;
  initialize();
  while (1) {
    printmenu();
    puts("choice :");
    scanf("%d", &choice);
    if (choice == 1)
      add();
    else if (choice == 2)
      view();
    else if (choice == 3)
      delete ();
    else if (choice == 4)
      exit(0);
    else
      puts("Invalid choice");
  }
  return 0;
}