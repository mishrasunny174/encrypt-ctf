#include<stdio.h>
#include<unistd.h>

void shell(){
	system("/bin/bash");
}

int main(){
	char buffer[128];
	setvbuf(stdout, NULL, _IONBF, 0);
	printf("Tell me your name: ");
	gets(buffer);
	printf("Hello, %s\n",buffer);
	//shell();
	return 0;
}
