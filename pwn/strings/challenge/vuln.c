#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <wchar.h>
#include <locale.h>

void vuln(){
  char buffer[128];
  int i = 0;
  for (i = 0; i<3 ; i++){
  fgets(buffer, sizeof(buffer), stdin);
   printf(buffer);
    puts("");

  }
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);

  printf("Heres a gift for ya %p \n",system);

  vuln();
  return 0;
}