#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define Levels 1000


void win(){
  char flag[120];

    FILE *flag_file = fopen("./flag.txt", "r");

    if (flag_file == NULL) {
        puts("Create a flag.txt locally");
        exit(-1);
    }

    fread(flag, 1, sizeof(flag) - 1, flag_file);
    fclose(flag_file);
    printf("Congratulations! You're the Cards Master! Here's the flag: %s\n", flag);
    exit(0);
}

void disable_buffering(void) {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

int main(void){
    srand(time(0)+0xfe);
    disable_buffering();
    int hole;
    int monkey;
    int cheats;


    puts("Welcome to the Alphabet Card Game!");
    puts("You're in a room with a deck of cards, each representing a letter of the alphabet.");
    puts("A mysterious figure is hiding behind one of the cards, waiting to reveal a letter.");
    puts("Your task is to guess the correct letter before it's unveiled.");

    for (int i=0;i<Levels;i++){
    puts("Make a guess");
    scanf("%d",&hole);
    cheats = rand();
    monkey = ((cheats % 26 + 65) ^ (cheats % 26) + 0xfefe);
    if (monkey == hole){
      printf(" [%d] More !\n",Levels-i-1);
    }else{
      puts("You Lose !");
      exit(0);
    }
    }
    win();
}
