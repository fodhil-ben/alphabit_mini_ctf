#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void win(int check) {
    char flag[64];

    FILE *flag_file = fopen("./flag.txt", "r");

    if (flag_file == NULL) {
        perror("Error opening flag file");
        exit(-1);
    }

    fread(flag, 1, sizeof(flag) - 1, flag_file);
    fclose(flag_file);

    if (check==0x1412)
        printf("Congratulations, here is your flag: %s\n",flag);
    else
        printf("You were close; try again");
}


__asm__("pop %rdi; ret");

void vuln(void) {
    char buffer[48];
    int local_check;
    printf("Enter your input: ");
    gets(buffer);   
    if (local_check == 0x4a55)
    return ;
    else 
    exit(0);

}

void setup(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

int main() {

    setup();
    vuln();    
    exit(0);
}
