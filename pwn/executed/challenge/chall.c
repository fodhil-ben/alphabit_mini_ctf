// gcc - zexecstack../ src / chall.c - o chall
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

void menu(void);
void hello_world(void);
void printCurrentDate(void);
void execute(void (*user_input)());
void generateRandomNumber(void);
void disable_buffering(void);

int main(void)
{
    disable_buffering();
    menu();
    char choice[50];
    scanf("%s", choice);
    if (strcmp(choice, "hello_world") == 0)
    {
        hello_world();
    }
    else if (strcmp(choice, "date") == 0)
    {
        printCurrentDate();
    }
    else if (strcmp(choice, "random") == 0)
    {
        generateRandomNumber();
    }
    else if (strcmp(choice, "exit") == 0)
    {
        return 0;
    }
    else
    {
        execute(choice);
    }
}
void menu(void)
{
    printf("the program is simple you enter the name of the function and i execute\n");
    printf("choose a function from this from this\n");
    printf("hello_world\n");
    printf("today date\n");
    printf("generate a random\n");
    printf("exit\n");
    printf("You choice is\n");
}

void printCurrentDate()
{
    time_t t;
    struct tm *current_time;

    time(&t);
    current_time = localtime(&t);

    printf("Current Date: %02d-%02d-%04d\n",
           current_time->tm_mday, current_time->tm_mon + 1, current_time->tm_year + 1900);
}

void generateRandomNumber(void)
{
    srand((unsigned int)time(NULL));
    printf("%d\n", 0xc0de + rand() % (0xdead - 0xc0de + 1));
}

void hello_world(void)
{
    printf("hello world\n");
}

void execute(void (*user_input)())
{
    user_input();
}

void disable_buffering(void)
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}