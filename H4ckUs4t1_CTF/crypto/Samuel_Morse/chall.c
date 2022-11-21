#define _GNU_SOURCE

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#define UNIT 50000

const char *MORSE[] = {
	['a'] = ".-",
	['b'] = "-...",
	['c'] = "-.-.",
	['d'] = "-..",
	['e'] = ".",
	['f'] = "..-.",
	['g'] = "--.",
	['h'] = "....",
	['i'] = "..",
	['j'] = ".---",
	['k'] = "-.-",
	['l'] = ".-..",
	['m'] = "--",
	['n'] = "-.",
	['o'] = "---",
	['p'] = ".--.",
	['q'] = "--.-",
	['r'] = ".-.",
	['s'] = "...",
	['t'] = "-",
	['u'] = "..-",
	['v'] = "...-",
	['w'] = ".--",
	['x'] = "-..-",
	['y'] = "-.--",
	['z'] = "--..",
	['1'] = ".----",
	['2'] = "..---",
	['3'] = "...--",
	['4'] = "....-",
	['5'] = ".....",
	['6'] = "-....",
	['7'] = "--...",
	['8'] = "---..",
	['9'] = "----.",
	['0'] = "-----",
	['&'] = ".-...",
	['\''] = ".----.",
	['@'] = ".--.-.",
	[')'] = "-.--.-",
	['('] = "-.--.",
	['}'] = "-.--.-",
	['{'] = "-.--.",
	[':'] = "---...",
	[','] = "--..--",
	['='] = "-...-",
	['!'] = "-.-.--",
	['.'] = ".-.-.-",
	['-'] = "-....-",
	['_'] = "..--.-",
	['+'] = ".-.-.",
	['"'] = ".-..-.",
	['?'] = "..--..",
	['/'] = "-..-.",
};

void get_flag(char *flag, size_t len)
{
	FILE *f = fopen("flag.txt", "r");
	if (f == NULL) {
		puts("Couldn't open flag file! Please contact an admin.");
		exit(EXIT_FAILURE);
	}
	if (fgets(flag, len, f) == NULL) {
		puts("Couldn't read flag file! Please contact an admin.");
		exit(EXIT_FAILURE);
	}
	fclose(f);
}

void send_chr(char c, unsigned int times)
{
	for (unsigned int i = 0; i < times; i++) {
		putc(c, stdout);
		usleep(UNIT);
	}
}

void send(const char *msg)
{
	while (*msg) {
		if (*msg == ' ') {
			send_chr('\0', 4);
		} else {
			const char *s = MORSE[*msg];

			if (s != NULL)
			{
				while (*s) {
					if (*s == '-')
						send_chr('\7', 3);
					else
						send_chr('\7', 1);
					send_chr('\0', 1);
					s++;
				}
				send_chr('\0', 2);
			}
		}
		msg++;
	}
}

int main()
{
	setbuf(stdout, NULL);

	char flag[64];
	get_flag(flag, sizeof(flag));

	char *msg = NULL;
	if (asprintf(&msg, "%s", flag) == -1) {
		puts("Couldn't allocate memory! Please contact an admin.");
		exit(EXIT_FAILURE);
	}
	send(msg);
	free(msg);
}
