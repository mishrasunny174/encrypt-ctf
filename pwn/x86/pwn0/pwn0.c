#include<unistd.h>
#include<stdio.h>
#include<string.h>

void print_flag(){
	system("cat flag.txt");
}

int main(){
	char josh[4];
	char buffer[64];
	setvbuf(stdout,NULL,_IONBF,0);
	printf("How's the josh?\n");
	gets(buffer);
	if(memcmp(josh,"H!gh",4)==0) {
		printf("Good! here's the flag\n");
		print_flag();
	} else {
		printf("Your josh is low!\nBye!\n");
	}
	return 0;
}
