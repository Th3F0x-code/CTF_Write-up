#include <stdio.h>
#include <stdarg.h>
#include <cstring>

char flag[512];
char password[] = "1Mp0ssible_t0_break_th3_p4ssw0rd";

bool is_printable( char c )
{
    return !( c & (1 << 7) );
}

void c(char *buf, ...)
{
	va_list args;
	va_start (args, buf);    

	char arg = va_arg(args, int);
	
	while( arg ) {
		sprintf(buf, "%s%c", buf, arg);
		arg = va_arg(args, int);
	}

	va_end (args);                  
}

void print_flag(int check){
	c(flag,'I', 'T', 'T', '{', '1', '_', 'H', '4', 't', '3', '_', 'y', '0', 'U', '_', 's', '0', '_', 'M', 'u', 'C', 'h', '1', '1', '!', '}');
	if(check == 0xcafebabe){
		printf("I hate you...\n");
		puts(flag);
	}else{
		printf("Unlucky...\n");
	}
}

int main(){
 	
	char input[32];
	printf("Welcome to the new safe check!\n");
	printf("Only authorized users can enter.\n");
	printf("Enter your password: ");
	scanf("%s", input);
	if(strcmp(input, password) == 0){        
		printf("Access granted!\n");
		printf("Today you can't steal my flag :P\n");
		return 0;
	}else{
		printf("Access denied!\n");
	}
}
