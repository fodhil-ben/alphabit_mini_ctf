#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void win(int check)
{

    if (check == 0x1412)
        system("/bin/sh");
    else
        printf("You were close; try again");
}

void vuln(void)
{
    char buffer[48];
    int local_check;
    printf("Enter your input: ");
    gets(buffer);
    if (local_check == 0x4a55)
    {
        puts("Got One");
        return;
    }
    else
    {
        exit(0);
    }
}

void setup()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main()
{

    setup();
    vuln();
    return 0;
}
