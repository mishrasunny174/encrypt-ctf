#include <stdio.h>
#include <string.h>
#include <unistd.h>

void run_command_ls() {
	system("ls");
}

void lol() {
	__asm__("jmp %esp");
}

int main(){
	char buffer[32];
	setvbuf(stdout, NULL,_IONBF,0);
	printf("$ ");
	gets(buffer);
	if(strcmp(buffer,"ls")==0) {
		run_command_ls();
	} else {
		printf("bash: command not found: %s\n",buffer);
	}
	printf("Bye!\n");
	return 0;
}
