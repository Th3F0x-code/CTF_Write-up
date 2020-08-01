#include <stdio.h>
#include <string.h>


void getInput(char * buffer){
    int count = 0;
    char c = '1';

    while (count < 64) {
        c = getchar();
        if (c!='\n'&&c!=EOF){
            buffer[count] = c;
            count ++;
        }else{
            break;
        }
    }
    buffer[count]=0x00;
    
    if(count >= 64){
        while ((c = getchar()) != '\n' && c != EOF);
    }
}

void build(){
    
    char result[256];
    char third[64];
    char second[64];
    char first[64];
    memset(result,0,sizeof(result));
    
    puts("Insert the protocol:");
    getInput(first);
    puts("Insert the domain:");
    getInput(second);
    puts("Insert the path:");
    getInput(third);

    strcat(result, first);
    strcat(result, "://");
    strcat(result, second);
    strcat(result, "/");
    strcat(result, third);

    puts("Result:");
    printf("%s\n", result);
}

int main()
{
    puts("Welcome to the URL builder");
    char next = 'y';
    while (next == 'y' || next == 'Y')
    {
        build();
        puts("Build another URL? [y/n]");
        scanf("%c", &next);
        getchar();
    }
    puts("Thanks for using our tool!");
}

