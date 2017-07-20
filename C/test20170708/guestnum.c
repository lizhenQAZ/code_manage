#include "stdio.h"
#include "stdlib.h"
#include "time.h"
int main(int argc, char const *argv[])
{
	srand(time(NULL));
	int realvaule=rand()%6;
	printf("please enter integer number in 0-6:\n");
	while(1)
	{
		int inputvalue;
		scanf("%d",&inputvalue);
		if (inputvalue<realvaule)
		{
			printf("too low!\n");
		}
		else if (inputvalue>realvaule)
		{
			printf("too high!\n");
		}
		else
		{
			printf("correct!\n");
			break;
		}
	}
	printf("exit\n");
	return 0;
}