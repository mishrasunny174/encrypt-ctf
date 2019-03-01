#include <stdio.h>
#include <stdlib.h>

//"encryptCTF{gdb_or_r2?}"

int main(int argc, char *argv[])
{
	char key[20];
	printf("Enter The Secret Code To Open the Vault: ");
	fgets(key,20,stdin);
	printf("\nFlag: ");
	if(key[1]==0x44)
	{
		printf("en");
		if(key[2]==0x44)
		{
			printf("cryptCTF{BYE}");
			exit(0);
		}
		else if(key[2]==0x01)
		{
			printf("cry");
			if(key[3]==0x41)
			{
				printf("ptC");
				if(key[5]==0x20)
				{
					printf("TF{");
					if(key[6]==0x21)
					{
						printf("gdb");
						if(key[8]==0x65)
						{
							printf("_or");
							if(key[9]==0x19	)
							{
								printf("_r2?");
								if(key[10]==0x09)
								{
									printf("}\n");
								}
								else
								{
									exit(0);
								}
							}
							else
							{
								exit(0);
							}

						}
						else
						{
							exit(0);
						}
					}
					else
					{
						exit(0);
					}
				}
				else
				{
					exit(0);
				}
			}

			
			else
			{
				exit(0);
			}
		}
	}
	return 0;
}