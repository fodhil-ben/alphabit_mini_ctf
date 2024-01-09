#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stddef.h>




void init() {
    alarm(120);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}


void vuln(){
    char buffer[128]={0};
    char flag[128];

    init();


    FILE *flag_file = fopen("./flag.txt", "r");

    if (flag_file == NULL) {
        puts("Create a flag.txt locally");
        exit(-1);
    }

    size_t length = fread(flag, 1, 120 - 1, flag_file);
    fclose(flag_file);
    
     scanf("%128s",buffer);
    if (strncmp(buffer,flag,length) == 0 ){
        system("/bin/sh");
    }else{
        puts("You have to know it \n");
    }



}

int main(){

    puts("Welcome to our system");
    vuln();
    return 0;

}
