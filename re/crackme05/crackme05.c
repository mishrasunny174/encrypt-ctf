#include <stdio.h>

#define FLAGSIZE 31

int readflag(int i2) {
  char flag[31] = "\x08\x03\x0e\x1f\x14\x1d\x19.9+\x16,\x01\n\x02\x1f\x04\x19\x05\x00\x1e@\x03\x02\x19@\x08\x0c\x1e\x14\x10";
  for ( int i= 0; i < FLAGSIZE; i++) {
    printf("%c", flag[i]^i2);
  }
  return 0;
}

int main() {
  int i2 = 0;
  char password[9];
  char username[9];
  printf("Hey give username\n");
  
  read(0, username, 8);
  
  printf("Give pass:\n");
  read(0, password, 8);
  char result[9];
  
  for (int i = 0; i < 9;i++){
    result[i] = password[i] ^ username[i];
  }
  for (int i = 0; i < 9;i++) {
    i2 += result[i]-(i*4);
  }
  readflag(i2);
  
  return 0;
}

