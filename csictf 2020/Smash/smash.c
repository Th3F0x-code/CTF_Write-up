#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void say_hello(char *arg1)
{
	char name[128];
	strcpy(name, arg1);
	printf("Hello, ");
        printf(name);
        printf("!\n");
	return;
}

int main()
{
	setbuf(stdout, NULL);
	setbuf(stdin, NULL);
	setbuf(stderr, NULL);
	int size = 0;
	char *arg1 = (char*) malloc(0);
	printf("What's your name?\n");
	while (1)
	{
		char temp;
		scanf("%c", &temp);
		++size;
		arg1 = (char*) realloc(arg1, size* sizeof(char));
		if (temp == '\n')
		{
			arg1[size - 1] = '\0';
			break;
		}
		else
		{
			arg1[size - 1] = temp;
		}
	}
	say_hello(arg1);
	free(arg1);
	return 0;
}
