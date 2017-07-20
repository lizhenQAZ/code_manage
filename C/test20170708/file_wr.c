#include "stdio.h"

int main(int argc, char const *argv[])
{
	/*
	FILE *f=fopen("data.txt","w");
	if (f!=NULL)
		{
			for (int i = 0; i < 100; i++)
			{
				fprintf(f,"hello %d\n",i);
			}
		}	
	fclose(f);
	return 0;
	*/

	FILE *f=fopen("data.txt","r");
	fseek(f,0,SEEK_END);
	long size=ftell(f);
	char buf[size+1];
	fseek(f,0,SEEK_SET);
	fread(buf,sizeof(unsigned char),size,f);
	buf[size]='\0';
	fclose(f);
	printf("%s", buf);
	return 0;
}