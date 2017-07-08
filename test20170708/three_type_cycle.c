#include "stdio.h"
int main(int argc, char const *argv[])
{
	/*
	int i = 0;
	for (; i < 100; printf("%d\n", i++))
	{
		printf(">>>\n");
	}
	return 0;
	*/

	/*
	int i=0;
	while(i<100)
	{
		printf("%d\n",i);
		i++;
	}
	return 0;
	*/

	int i=0;
	do
	{
		printf("%d---\n",i);
		i++;
	}
	while(i<100);
	return 0;
}