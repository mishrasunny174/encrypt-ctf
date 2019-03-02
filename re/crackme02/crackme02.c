#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

void print_flag() {
	system("cat flag.txt");
}

void goBoom() {
	printf("BOOM!\nBye!\n");
	exit(0);
}

void functionZero(char* buffer) {
	if(strcmp(buffer,"CRACKME02")!=0) {
		goBoom();
	}
}

void functionOne(char* buffer) {
	int magicNumber = 0xdeadbeef;
	if(*(int*)buffer!=magicNumber) {
		goBoom();
	}
}

void functionTwo(char* buffer) {
	int i=0;
	char string[] = "ZXytUb9fl78evgJy3KJN";
	for(i=0;i<strlen(string);i++) {
		if(string[i]!=buffer[i]) {
			goBoom();
		}
	}
}

void functionThree(char* buffer) {
	if(strlen(buffer)>3)
		goBoom();
	int one = atoi(buffer);
	if((one*one*one)+(4*(one*one)-(2*one)-3)==0)
		{
			printf("SUBSCRIBE TO PEWDIEPIE\n");
		}
	else
	{
		goBoom();
	} 
}

void functionFour(char* buffer) {
	char buffer2[10];
	strncpy(buffer2,buffer,10);
	printf("Validating Input 4\n");
	if(buffer2[0]+buffer2[8]==213)
	{
		if(buffer2[1]+buffer2[7]==206)
		{
			if(buffer2[2]+buffer2[6]==231)
			{
				if(buffer2[3]+buffer2[5]==201)
				{
					if(buffer2[4]==105)
						printf("you earned it\n");
				}
				else
					goBoom();
			}
			else
				goBoom();
		}
		else
			goBoom();
	}
	else
		goBoom();
}

int main() {
	char buffer[64];
	void(*functionArray[])(char*) = {&functionZero,&functionOne,&functionTwo,&functionThree,&functionFour};
	void(*func)(char*);
	int i;
	setvbuf(stdout,NULL,_IONBF,0);
	printf("Hi!, i am a BOMB!\nI will go boom if you don't give me right inputs\n");
	for(i=0; i<5; i++) {
		printf("Enter input #%d: ",i);
		scanf("%s",buffer);
		func = functionArray[i];
		func(buffer);
	}
	print_flag();
	return 0;
}
