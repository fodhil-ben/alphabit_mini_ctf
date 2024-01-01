#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char input[100];

    FILE *f = fopen("flag.txt", "r");
    char buf[50];
    if (f == NULL)
    {
        printf("flag.txt not found \n");
        exit(0);
    }
    fgets(buf, 50, f);
    fclose(f);

    fgets(input, 50, stdin);
    printf(input);
}
