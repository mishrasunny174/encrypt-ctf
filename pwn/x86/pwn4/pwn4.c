#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void __() {
	system("/bin/bash");
}

int main(){
	char buffer[128];
	setvbuf(stdout, NULL, _IONBF, 0);	
	puts("Do you swear to use this shell with responsility by the old gods and the new?\n");
	gets(buffer);
	printf(buffer);
	printf("\ni don't belive you!\n%s\n",buffer);
	return 0;
}
