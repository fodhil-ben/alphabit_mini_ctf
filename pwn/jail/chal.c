#include <stdio.h>
#include <stdlib.h>


void disable_buffering(void) {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

int main(){
    disable_buffering();
    char buffer[120];
    char flag[120];

    FILE *flag_file = fopen("./flag.txt", "r");

    if (flag_file == NULL) {
        puts("Create a flag.txt locally");
        exit(-1);
    }

    fread(flag, 1, sizeof(flag) - 1, flag_file);
    fclose(flag_file);

     fgets(buffer, sizeof(buffer), stdin);
    
    if (strcmp(buffer,flag,120) == 0 ){
        printf("%s : \n",flag);
    }else{
        puts("You have to know it \n");
    }
}