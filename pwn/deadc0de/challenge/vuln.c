#include <stdio.h>
#include <stdlib.h>

void setup() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}


int main(void){

    setup();

    char br[60];
    int pass1;
    char wall[40] = "You shall not pass ";
    int pass2;
    
    printf("Give me what you need: ");
    gets(br);

    if ((pass1 == 0xd3adc0d3) && (pass2 == 0xb1d5e9a2))
    system("/bin/sh");
    else
    printf("better luck next time");

    return 0;
}