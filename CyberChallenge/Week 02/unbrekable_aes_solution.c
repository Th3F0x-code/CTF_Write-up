#include <stdio.h>


char ror(char c,int index) {
   unsigned char tmp1, tmp2;
   
    for(int i = 0; i < index; i++) {
        tmp1 = c;
        tmp2 = c;
        tmp1 = tmp1 << 1;
        tmp2 = tmp2 >> 7;
        c = tmp1 | tmp2;
    }
   
    return c;
}


int main() {
   FILE* in = fopen("flag.txt.aes", "rb");
   unsigned char dati[2];
   unsigned int i = 0, val;
   
   do {
        val = fread(dati, sizeof(char), 1, in);
      
        for(int x = 0; x < val; x++) {
            i += 1;
            dati[x] = ror(dati[x], i);
        }
      
        dati[val] = '\0';
        printf("%s ", dati);
      
    } while(val > 0);
   
   
    return 0;
}
