#include <stdio.h>
#include <stdlib.h>
#include <string.h>



void disable_buffering(void) {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}



void vuln(void){
    char buffer[64];

    while (1){
    puts("what do you want: ");
    gets(buffer);

    if(!strncmp(buffer,"leave", 5)){
        puts("have it your way");
        return;
    }

    printf(buffer);
    puts("\n");
    }
}


int main(void){

    disable_buffering();
    system("echo 'No more Gifts for you \n'");

    vuln();
    return 0;
}



